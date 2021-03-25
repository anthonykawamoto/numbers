# AutoScaling API
This application is a minimal autoscaling API which connects with a data source, queries it and returns the result to the consumer.

* for the autoscaling component, the solution leverages AWS Lambda
* AWS DynamoDB is used as the data storage layer
* the data access layer is represented by AWS API Gateway

## Development Dependencies
* AWS SAM
* AWS CloudFormation
* Python 3.7

## Usage
To the deploy the application to AWS:
```bash
# export AWS keys
export AWS_ACCESS_KEY_ID=xxxxx
export AWS_SECRET_ACCESS_KEY=xxxxx

# trigger the CloudFormation deploy
bin/deploy.sh
```
