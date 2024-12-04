from aws_cdk import Stack, aws_ec2 as ec2, aws_iam as iam
from constructs import Construct

class EC2AppStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        existing_role = iam.Role.from_role_arn(self,
                                               "DemoRoleForEC2",
                                               "arn:aws:iam::051731307098:role/DemoRoleForEC2",
                                                mutable=False)
        instance_type = ec2.InstanceType("t2.micro")  
        machine_image = ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2)
        vpc = ec2.Vpc.from_lookup(self, "Vpc",vpc_id="vpc-0619390fdcaff023b")
        
        ssh_in_security_group = ec2.SecurityGroup.from_security_group_id(self,
                                                                         "ssh-in",
                                                                         "sg-04ecc805275e5409f",
                                                                         mutable=False)

        instance = ec2.Instance(self, "MyEC2Instance",
                                instance_type=instance_type,
                                machine_image=machine_image,
                                role=existing_role,
                                vpc=vpc,
                                key_name="ssh keypair",
                                security_group=ssh_in_security_group)
