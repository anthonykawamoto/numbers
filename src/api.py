import json
import logging
import db

logger = logging.getLogger()


def handler(event, _):
    try:
        target_id = event['queryStringParameters']['id']
    except KeyError:
        return {
            'statusCode': 400
        }

    item = db.get(target_id)

    return {
        'statusCode': 200,
        'body': json.dumps({'reversed': item['reversed']})
    }
