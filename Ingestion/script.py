import boto3
import os
from datetime import datetime

s3 = boto3.client('s3')

bucket_name = 'olist-raw-ap-south-1'
local_folder = r"C:\Users\mvshraddha\Documents\olist_datasets"

# Get today's date
today_date = datetime.today().strftime('%Y-%m-%d')

print("Uploading to:", f"raw-data/{today_date}/")

for root, dirs, files in os.walk(local_folder):
    for file in files:
        if file.endswith('.csv'):
            local_path = os.path.join(root, file)

            # IMPORTANT: this line creates the date folder
            s3_key = f"raw-data/{today_date}/{file}"

            print("DEBUG S3 PATH:", s3_key)   # 👈 check this

            s3.upload_file(local_path, bucket_name, s3_key)

print("Done 🚀")