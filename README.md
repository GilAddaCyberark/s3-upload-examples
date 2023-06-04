# Examples for uploading files to s3 

## AWS SDK with boto3 
in this folder you will find ways to upload files using 

* Direct upload using boto3 Python client
* Creating a pre-signed URL and upload the file usign a web client

## AWS Transfer family 
In this folder you will find an example of creating an 
AWS Transfer Family endpoint server that provides S3 access using SFTP Protocol

To create an AWS Transfer family endpoint you need the follwign pre-requisites:
* AWS CLI is installed
* AWS account credentials are set to your account

replace the command bucket name with your S3 bucket name and run the following commands:
``` bash
cd aws-transfer-family
aws cloudformation deploy --template-file aws-transfer-family-cf-template.yaml --stack-name aws-transfer-family-stack \ 
--capabilities CAPABILITY_NAMED_IAM --parameter-overrides s3bucketName='your-bucket-name'
```
After a successful  setup, you will have a:
Server with SFTP protocol defined and a custom AWS Lambda that performs the authentication.
Warningw: 
1. The current code provides access, with a placeholder for password verification code.
You should add the integration with the IdP an authentication code there.
2. Deploying content will add AWS charges for creating or using AWS chargeable resources. Delete the stack to avoid additional charges.

to list the AWS Transfer Family servers and get server endpoint go to the AWW Console in the AWS Transfer service

To use the SFTP server run this command
```bash
sftp my-user@server-id.server.transfer.us-east-1.amazonaws.com
```
once you get the propmpt enter ypur password and perform SFTP commands as:
```
sftp> pwd
sftp> put local-file-path
sftp> ls
```