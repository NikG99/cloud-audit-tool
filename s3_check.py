# Sample check for public S3 buckets
import boto3

def check_public_s3_buckets():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()['Buckets']
    for bucket in buckets:
        acl = s3.get_bucket_acl(Bucket=bucket['Name'])
        for grant in acl['Grants']:
            if 'AllUsers' in str(grant['Grantee']):
                print(f"[!] Public bucket found: {bucket['Name']}")
