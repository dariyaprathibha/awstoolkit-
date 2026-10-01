import boto3

# Simple EC2 status checker for support
ec2 = boto3.client('ec2', region_name='ap-south-1')
response = ec2.describe_instances()

for r in response['Reservations']:
    for inst in r['Instances']:
        print(f"ID: {inst['InstanceId']} - State: {inst['State']['Name']}")