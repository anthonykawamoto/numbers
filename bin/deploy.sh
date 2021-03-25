#!/usr/bin/env bash

ARTIFACTS_BUCKET=${ARTIFACTS_BUCKET:-numbers-lambda-artifacts}


sam build --use-container
sam package \
    --template-file .aws-sam/build/template.yaml \
    --output-template-file packaged.yaml \
    --s3-bucket ${ARTIFACTS_BUCKET}
sam deploy \
    --template-file ./packaged.yaml \
    --stack-name numbers \
    --capabilities CAPABILITY_IAM
