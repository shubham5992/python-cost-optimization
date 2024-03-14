import boto3

# Create an S3 client
s3_client = boto3.client('s3')

# Specify the name of the bucket you want to create
bucket_name = 'my-new-bucket'

# Create the bucket
response = s3_client.create_bucket(
    Bucket='my-first-yt-vucket-name2323'
  
)