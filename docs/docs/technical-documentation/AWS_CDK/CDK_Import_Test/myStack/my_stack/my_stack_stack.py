from aws_cdk import Stack
import aws_cdk as cdk
import aws_cdk.aws_s3 as s3
from constructs import Construct


class MyStackStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Resources
        s3Bucket00879800366101gmfqgnylayyejakjfomjkf00B0vFt = s3.CfnBucket(
            self,
            "S3Bucket00879800366101gmfqgnylayyejakjfomjkf00B0VFt",
            public_access_block_configuration={
                "restrictPublicBuckets": True,
                "ignorePublicAcls": True,
                "blockPublicPolicy": True,
                "blockPublicAcls": True,
            },
            bucket_name="879800366101-gmfqgnylayyejakjfomjkf",
            ownership_controls={
                "rules": [
                    {
                        "objectOwnership": "BucketOwnerEnforced",
                    },
                ],
            },
            bucket_encryption={
                "serverSideEncryptionConfiguration": [
                    {
                        "bucketKeyEnabled": False,
                        "serverSideEncryptionByDefault": {
                            "sseAlgorithm": "AES256",
                        },
                    },
                ],
            },
        )
        s3Bucket00879800366101gmfqgnylayyejakjfomjkf00B0vFt.cfn_options.deletion_policy = (
            cdk.CfnDeletionPolicy.RETAIN
        )
