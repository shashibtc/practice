import boto3
import os
from dotenv import load_dotenv

load_dotenv() # This loads the .env file with our environment variables

directory = "files" # file to be uploaded to s3
bucket_name = "dev-appinsights-data-lake"

s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

for file_name in os.listdir(directory):
    try:
        response = s3_client.upload_file(file_name, bucket_name, file_name)
        print(f"Successfully copied {file_name}")
    except Exception as ex:
        print(f"Something went wrong while copying the {file_name} to S3, Exception details are:::{ex}")
        