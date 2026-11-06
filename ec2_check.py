import boto3

# Connect to EC2
ec2 = boto3.client('ec2', region_name='ap-south-1')

# List all EC2 instances
response = ec2.describe_instances()

print("--- EC2 Instance Status ---")
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"ID: {instance['InstanceId']} | State: {instance['State']['Name']}")