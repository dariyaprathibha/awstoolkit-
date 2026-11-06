import boto3

iam = boto3.client('iam')
print("--- IAM Users List ---")

response = iam.list_users()
for user in response['Users']:
    print(f"User: {user['UserName']} | Created: {user['CreateDate']}")