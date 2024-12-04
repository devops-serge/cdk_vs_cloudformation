#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_app.ec2_app_stack import EC2AppStack

env = cdk.Environment(
    account=os.environ.get('CDK_DEFAULT_ACCOUNT'),  # Retrieve from environment variable
    region=os.environ.get('CDK_DEFAULT_REGION')     # Retrieve from environment variable
)

app = cdk.App()
EC2AppStack(app, "EC2AppStack", env=env)

app.synth()
