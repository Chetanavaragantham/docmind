import boto3

sts = boto3.client('sts')
assumed = sts.assume_role(
    RoleArn='arn:aws:iam::601063789997:role/DocMind-S3-ReadOnly-Role',
    RoleSessionName='test-session'
)

creds = assumed['Credentials']
s3_restricted = boto3.client(
    's3',
    aws_access_key_id=creds['AccessKeyId'],
    aws_secret_access_key=creds['SecretAccessKey'],
    aws_session_token=creds['SessionToken']
)

bucket_name = 'docmind-chetanavaragantham-2026'

# This should succeed (read)
response = s3_restricted.list_objects_v2(Bucket=bucket_name)
print("List succeeded:")
for obj in response.get('Contents', []):
    print(" -", obj['Key'])

# This should FAIL (write) — that's the point of today
try:
    s3_restricted.upload_file('test.txt', bucket_name, 'should-fail.txt')
    print("Upload succeeded (this shouldn't happen!)")
except Exception as e:
    print("\nUpload failed as expected:")
    print(e)
