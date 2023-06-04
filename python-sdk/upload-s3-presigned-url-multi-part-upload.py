#!/usr/bin/env python
"""
This is a demo of Multipart Upload using AWS Python SDK -boto3 library.

This module provides high level abstractions for efficient
uploads/download.

* Automatically switching to multipart transfer when
  a file is over a specific size threshold
* Uploading/downloading a file in parallel
* Progress callbacks to monitor transfers

Credits to: ANKHI PAUL
"""
import argparse
import os

import boto3
from boto3.s3.transfer import TransferConfig

s3_resource = boto3.resource('s3')


# Function to upload the file to s3 using multipart functionality
def multipart_upload_boto3(local_file_path: str, bucket_name: str, object_key: str):

    config = TransferConfig(
        multipart_threshold=1024 * 1,  #Ensure multipart if the size of a transfer is larger than 1 MB
        max_concurrency=10,
        multipart_chunksize=1024 * 1,  # multipart_chunksize : Each part size is of 1 MB
        use_threads=True)

    s3_resource.Object(bucket_name, object_key).upload_file(local_file_path, ExtraArgs={'ContentType': 'image/jpg'}, Config=config)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('upload-s3-presigned-url-multi-part-upload')
    parser.add_argument('-b', '--bucket', help='AWS S3 bucket name to upload files to')
    parser.add_argument('-k', '--key', help='AWS S3 object key to upload')
    args = parser.parse_args()
    file_path = os.path.join(os.path.dirname(__file__), os.pardir, "demo-image.jpg")
    multipart_upload_boto3(local_file_path=file_path, bucket_name=args.bucket, object_key=args.key)
