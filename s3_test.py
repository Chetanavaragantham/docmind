import boto3

s3 = boto3.client('s3')
bucket_name = 'docmind-chetanavaragantham-2026'

# Upload a file
with open('test.txt', 'w') as f:
    f.write('Hello from Day 1!')

s3.upload_file('test.txt', bucket_name, 'test.txt')
print("Uploaded.")

# List objects in the bucket
response = s3.list_objects_v2(Bucket=bucket_name)
for obj in response.get('Contents', []):
    print(obj['Key'], obj['Size'])

# Download it back under a new name
s3.download_file(bucket_name, 'test.txt', 'test_downloaded.txt')
print("Downloaded.")
