import boto3

# Create an S3 client with your credentials
s3_client = boto3.client(
    's3',
    aws_access_key_id='AKIAYCJIRBOHKR3QDAYL',
    aws_secret_access_key='lmyk5RbO5LKFlOpXChexbTXD3MifTDQnUjaxfdui'
)

# List the buckets
response = s3_client.list_buckets()
print("Buckets:")
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

# List the objects in a specific bucket
bucket_name = 'your-bucket-name'
response = s3_client.list_objects_v2(Bucket=bucket_name)
if 'Contents' in response:
    for obj in response['Contents']:
        print(f'  {obj["Key"]}')
else:
    print(f'No objects found in bucket {bucket_name}')
