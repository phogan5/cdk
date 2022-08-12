
from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as s3,
    aws_ec2 as ec2,
)
from constructs import Construct

class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cdk_bucket = s3.Bucket (self, 'MyBucket',
                                    block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
                                    versioned = False
                                    #Tags.of(bucket).add("Description", "This bucket was made using CDK")
        )

