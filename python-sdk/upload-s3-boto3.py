#!/usr/bin/env python
"""
This is an example

"""

import argparse

import boto3


def upload_file(bucket_name: str, object_key: str):

    s3 = boto3.resource(service_name='s3')

    bucket = s3.Bucket(bucket_name)
    bucket.upload_file(Filename='./../myfile.txt', Key=object_key)


if __name__ == '__main__':

    try:
        parser = argparse.ArgumentParser('upload-s3-boto3')
        parser.add_argument('-b', '--bucket', help='AWS S3 bucket name to upload files to')
        parser.add_argument('-k', '--key', help='AWS S3 object key to upload')
        args = parser.parse_args()

        upload_file(bucket_name=args.bucket, object_key=args.key)

    except Exception as ex:
        print(f'exception raised: {ex}')
