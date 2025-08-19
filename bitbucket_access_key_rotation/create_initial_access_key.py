"""Create the initial AWS Access Key and store in Bitbucket pipeline variables."""

import json
import logging

import boto3
import requests

logger = logging.getLogger()
logger.setLevel("INFO")

PIPELINE_USER = "terraform-pipeline-user"
BITBUCKET_ACCESS_TOKEN_PATH = "bitbucket_access_tokens"
TERRAFORM_USER_SECRET_PATH = "terraform-pipeline-user_access_keys"
BITBUCKET_VARIABLE_UUIDS_SECRET_PATH = "bitbucket_repo_variable_uuids"
BITBUCKET_WORKSPACE = "MY_BITBUCKET_WORKSPACE"
REPOSITORY_LIST = ["MY_REPOSITORY_1", "MY_REPOSITORY_2"]
REGION = "eu-west-1"


def create_aws_access_key(pipeline_iam_username, region, terraform_user_secret_name):
    """
    Create AWS Access keys for the pipeline user and store in secrets manager.
    Parameters:
      pipeline_iam_username (str): The IAM user used in the terraform pipeline
      region (str): The region for the secrets
      terraform_user_secret_name (str): The Secret name for the terraform user access keys
    """
    iam_client = boto3.client("iam")
    secrets_client = boto3.client("secretsmanager", region_name=region)
    iam_response = iam_client.create_access_key(UserName=pipeline_iam_username)
    access_key_kv = {"AWS_ACCESS_KEY_ID": iam_response["AccessKey"]["AccessKeyId"]}
    secret_key_kv = {
        "AWS_SECRET_ACCESS_KEY": iam_response["AccessKey"]["SecretAccessKey"]
    }

    secrets_client.create_secret(
        Name=terraform_user_secret_name, SecretString=json.dumps(access_key_kv)
    )
    secrets_response = secrets_client.list_secrets(
        Filters=[
            {"Key": "name", "Values": [terraform_user_secret_name]},
        ],
    )
    secrets_client.update_secret(
        SecretId=secrets_response["SecretList"][0]["ARN"],
        SecretString=json.dumps(secret_key_kv),
    )


def get_bitbucket_access_token(repository_name, region, bitbucket_access_token_secret):
    """
    Get the Bitbucket Access token for the repository.
    Parameters:
        repository_name (str): The repository name.
        region (str): The region for the secrets
        bitbucket_access_token_secret (str): The secret which stores the Bitbucket access tokens
    """
    secrets_client = boto3.client("secretsmanager", region_name=region)

    response = secrets_client.get_secret_value(SecretId=bitbucket_access_token_secret)
    secret_key = f"access_token_{repository_name}"
    repo_access_token = eval(response["SecretString"])[secret_key]
    logging.info("Fetched the Bitbucket access token for %s", repository_name)
    return repo_access_token


def create_bitbucket_variable(
    bitbucket_workspace,
    repository_name,
    bitbucket_access_token,
    variable_key,
    variable_secured,
    region,
    terraform_user_secret_name,
    bitbucket_variable_uuids_secret_name,
):
    """
    Create the bitbucket variables.
    Parameters:
        bitbucket_workspace (str): The Bitbucket workspace name
        repository_name (str): The repository name.
        bitbucket_access_token (str): The Bitbucket access token
        variable_key (str): The variable to create. Allowed values:
            'AWS_ACCESS_KEY_ID'
            'AWS_SECRET_ACCESS_KEY'
        variable_secured (bool): Whether the variable is secured or not
        region (str): The region for the secrets
        terraform_user_secret_name (str): The Secret name for the terraform user access keys
        bitbucket_variable_uuids_secret_name (str): The Secret name for the bitbucket variable UUID
    """
    secrets_client = boto3.client("secretsmanager", region_name=region)
    secrets_response = secrets_client.list_secrets(
        Filters=[
            {"Key": "name", "Values": [terraform_user_secret_name]},
        ],
    )
    secret_response = secrets_client.get_secret_value(
        SecretId=secrets_response["SecretList"][0]["ARN"],
    )

    secret_value = eval(secret_response["SecretString"])[variable_key]
    logging.info("Fetched the %s", variable_key)

    url = f"https://api.bitbucket.org/2.0/repositories/{bitbucket_workspace}/{repository_name}/pipelines_config/variables"  # noqa: E501

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {bitbucket_access_token}",
    }

    payload = json.dumps(
        {
            "type": "string",
            "key": f"{variable_key}",
            "value": f"{secret_value}",
            "secured": variable_secured,
        }
    )

    response = requests.request("POST", url, data=payload, headers=headers, timeout=20)
    logger.info(
        json.dumps(
            json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")
        )
    )
    response_json = json.dumps(
        json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")
    )
    variable_uuid = json.loads(response_json)["uuid"][1:-1]

    secrets_response = secrets_client.list_secrets(
        Filters=[
            {"Key": "name", "Values": [bitbucket_variable_uuids_secret_name]},
        ],
    )
    secret_key_kv = {f"{variable_key}_uuid_{repository_name}": variable_uuid}
    secrets_client.update_secret(
        SecretId=secrets_response["SecretList"][0]["ARN"],
        SecretString=json.dumps(secret_key_kv),
    )


def create_initial_access_key(repository_list, region, terraform_user_secret_name):
    """
    Rotate keys then update Secrets and Bitbucket variables.
    Parameters:
        repository_list (list): The list of Repositories to update
        region (str): The region for the secrets
        terraform_user_secret_name (str): The secret name for the terraform user keys
    """
    create_aws_access_key(PIPELINE_USER, region, terraform_user_secret_name)

    for repository in repository_list:
        repo_access_token = get_bitbucket_access_token(
            repository, region, BITBUCKET_ACCESS_TOKEN_PATH
        )
        create_bitbucket_variable(
            BITBUCKET_WORKSPACE,
            repository,
            repo_access_token,
            "AWS_ACCESS_KEY_ID",
            False,
            region,
            terraform_user_secret_name,
            BITBUCKET_VARIABLE_UUIDS_SECRET_PATH,
        )
        create_bitbucket_variable(
            BITBUCKET_WORKSPACE,
            repository,
            repo_access_token,
            "AWS_SECRET_ACCESS_KEY",
            True,
            region,
            terraform_user_secret_name,
            BITBUCKET_VARIABLE_UUIDS_SECRET_PATH,
        )
