# AutoScaling API
This application is a minimal autoscaling API which connects with a data source, queries it and returns the result to the consumer. This API accepts a GET request (ie. /numbers?id=123) and returns the saved reversed id (ie. 321) 

* for the autoscaling component, the solution leverages AWS Lambda
* AWS DynamoDB is used as the data storage layer
* the data access layer is represented by AWS API Gateway

## Development Dependencies
* AWS SAM CLI
* Python 3.7
* Docker
* S3 bucket to host SAM artifacts

## Usage
To install the python lambda dependencies:
```bash
pip install -r src/requirements.txt
```

To test the lambda handler locally:
```bash
bin/test.sh
```

To the deploy the application to AWS:
```bash
# export AWS keys
export AWS_ACCESS_KEY_ID=xxxxx
export AWS_SECRET_ACCESS_KEY=xxxxx

# trigger the CloudFormation (SAM) deploy
bin/deploy.sh
```
