import boto3

client = boto3.client('s3')
response = client.get_bucket_acl(
    Bucket='my-first-yt-vucket-name2323'
 )

print(response)