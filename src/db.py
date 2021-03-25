import logging
import os
import boto3

logger = logging.getLogger()

try:
    dynamodb_table = os.environ['DYNAMODB_TABLE']
except KeyError as e:
    logger.error('Failed to load DYNAMODB_TABLE from environment variables')
    raise e

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(dynamodb_table)


def get(target_id):
    response = table.get_item(
        Key={
            'id': target_id
        }
    )
    item = response.get('Item')
    return item
