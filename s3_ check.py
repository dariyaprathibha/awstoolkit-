import boto3

s3 = boto3.client('s3')
print("--- S3 Buckets List ---")

response = s3.list_buckets()
for bucket in response['Buckets']:
    print(f"Bucket Name: {bucket['Name']}")