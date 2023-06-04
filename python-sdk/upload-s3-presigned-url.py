#!/usr/bin/env python
"""
This is an example

"""
# Example taken from: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html

import argparse
import logging

import boto3
import requests
from botocore.exceptions import ClientError


#
def create_presigned_post(bucket_name: str, object_key: str, fields=None, conditions=None, expiration=3600):
    """Generate a presigned URL S3 POST request to upload a file

    :param bucket_name: string
    :param object_name: string
    :param fields: Dictionary of prefilled form fields
    :param conditions: List of conditions to include in the policy
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Dictionary with the following keys:
        url: URL to post to
        fields: Dictionary of form fields and values to submit with the POST
    :return: None if error.
    """

    # Generate a presigned S3 POST URL
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_post(bucket_name, object_key, Fields=fields, Conditions=conditions, ExpiresIn=expiration)
    except ClientError as ex:
        logging.error(ex)
        return None

    # The response contains the presigned URL and required fields
    return response


if __name__ == '__main__':
    parser = argparse.ArgumentParser('upload-s3-presigned-url')
    parser.add_argument('-b', '--bucket', help='AWS S3 bucket name to upload files to')
    parser.add_argument('-k', '--key', help='AWS S3 object key to upload')
    args = parser.parse_args()

    response = create_presigned_post(bucket_name=args.bucket, object_key=args.key)
    logging.info(f'pre signed url: {response.get("url")}')

    # Demonstrate how another Python program can use the presigned URL to upload a file
    with open('../myfile.txt', 'rb') as f:
        files = {'file': (args.key, f)}
        http_response = requests.post(response['url'], data=response['fields'], files=files, timeout=10)

    logging.info(f'File upload HTTP status code: {http_response.status_code}')
