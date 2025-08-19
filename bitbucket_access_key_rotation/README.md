# AWS Access Key Rotation for Bitbucket Pipeline User

## Overview

We have a terraform pipeline role `terraform-pipeline-role` in each AWS account deployed via Cloudformation stacksets, this is used in the Bitbucket pipeline to run the terraform plan/apply.

There is a terraform pipeline user `terraform-pipeline-user` in the shared services account that has permissions to assume the terraform role in each AWS account.

The AWS Access and Secret key for the terraform user is stored in each repository as a variable, with the AWS Secret key being a secret variable.

This Python project uses **Boto3** to firstly create the AWS Access keys for `terraform-pipeline-user`, store the keys in each repository variable and store them locally in Secrets manager as well as the variable UUID which is needed to update existing bitbucket variables.

It then rotates AWS access keys for `terraform-pipeline-user`, updates the Bitbucket variables as well as the local AWS secrets

---

## Requirements

- `Python` 3.8+
- `Boto3`
- `Requests` (for Bitbucket API calls)
- Bitbucket repository access tokens with:
    - `pipeline:variable` permission
- AWS Account to store Secrets and run the Lambda function
- AWS Secret named `bitbucket_access_tokens` with:
    - Key Value Access tokens for each repository in the format `access_token_{repository_name}:Value`
- AWS Secret named `bitbucket_repo_variable_uuids` with:
    - Key Value Placeholder secrets for each repository in the format:
        - `AWS_ACCESS_KEY_ID_uuid_{repository_name}:Placeholder`
        - `AWS_SECRET_ACCESS_KEY_uuid_{repository_name}:Placeholder`
- AWS SNS Topic to send success notifications to
- AWS IAM permissions:
    - `iam:CreateAccessKey`
    - `iam:DeleteAccessKey`
    - `iam:ListAccessKeys`
    - `secretsmanager:ListSecrets`
    - `secretsmanager:GetSecretValue`
    - `secretsmanager:CreateSecret`
    - `secretsmanager:UpdateSecret`
    - `secretsmanager:PutSecretValue`
- Variables needed:
    - `BITBUCKET_WORKSPACE` (str) - The name of your Bitbucket Workspace
    - `REPOSITORY_LIST` (list) - The list of Bitbucket repositories
    - `REGION` (str) - The AWS Region
    - `SNS_TOPIC` (str) - The AWS SNS Topic to send notifications to

## Usage

The recommendation is to first run `create_initial_access_key.py` locally, this creates the initial Access/Secret Keys as well as the AWS Secret to store the keys.

`create_initial_access_key(repository_list, region, terraform_user_secret_name)`

To run the script `rotate_bitbucket_access_key.py` on a schedule it is recommended to create a Lambda function with an eventbridge trigger with the frequency of your choice.

We'd need to update the script to `import os` and to pull the below variables from the Lambda environment variables:

- os.environ['BITBUCKET_WORKSPACE']
- os.environ['REPOSITORY_LIST']
- os.environ['REGION']

## Script steps

### create_initial_access_key

- Create AWS Access Key for `pipeline_iam_username`
- Create AWS Secret `terraform_user_secret_name` and add `AWS_ACCESS_KEY_ID`
- Update AWS Secret `terraform_user_secret_name` and add `AWS_SECRET_ACCESS_KEY`
- Get bitbucket repository access token from `BITBUCKET_ACCESS_TOKEN_PATH`
- Pull `AWS_ACCESS_KEY_ID` from `TERRAFORM_USER_SECRET_PATH`
    - Add `AWS_ACCESS_KEY_ID` to repo variable
    - Get `UUID` of repo variable
    - Add `UUID` to `BITBUCKET_VARIABLE_UUIDS_SECRET_PATH` as `AWS_ACCESS_KEY_ID_uuid_{repository_name}`
- Pull `AWS_SECRET_ACCESS_KEY` from `TERRAFORM_USER_SECRET_PATH`
    - Add `AWS_SECRET_ACCESS_KEY` to repo variable
    - Get `UUID` of repo variable
    - Add `UUID` to `BITBUCKET_VARIABLE_UUIDS_SECRET_PATH` as `AWS_SECRET_ACCESS_KEY_uuid_{repository_name}`

### rotate_bitbucket_access_key

- Get `AWS_ACCESS_KEY_ID` for `PIPELINE_USER` from Secret `TERRAFORM_USER_SECRET_PATH`
- Delete existing IAM Access Key for `PIPELINE_USER`
- Create new Access keys for `PIPELINE_USER`
- Store the AWS Access key and Secret key in Secrets Manager
- For each repo:
    - Pull the bitbucket access token from Secrets Manager secret `BITBUCKET_ACCESS_TOKEN_PATH`
    - Get existing variable `AWS_ACCESS_KEY_ID` `UUID` from Secret `BITBUCKET_VARIABLE_UUIDS_SECRET_PATH`
    - Pull secret `AWS_ACCESS_KEY_ID` from Secret `TERRAFORM_USER_SECRET_PATH`
    - Update the repo variable `AWS_ACCESS_KEY_ID`
    - Get existing variable `AWS_SECRET_ACCESS_KEY` `UUID` from Secret `BITBUCKET_VARIABLE_UUIDS_SECRET_PATH`
    - Pull secret `AWS_SECRET_ACCESS_KEY` from `TERRAFORM_USER_SECRET_PATH`
    - Update the repo variable `AWS_SECRET_ACCESS_KEY`
- Send an SNS notification upon success
