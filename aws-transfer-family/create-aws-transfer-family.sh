#!/bin/bash
set -e

aws cloudformation deploy --template-file aws-transfer-family-cf-template.yaml \
--stack-name aws-transfer-family-stack --capabilities CAPABILITY_NAMED_IAM
