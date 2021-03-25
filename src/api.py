import json
import logging
import db

logger = logging.getLogger()


def render_successful_response(body):
    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }


def handler(event, _):
    try:
        target_id = event['queryStringParameters']['id']
    except KeyError:
        return {
            'statusCode': 400
        }

    item = db.get(target_id)
    if not item:
        return render_successful_response({})

    return render_successful_response({'reversed': item['reversed']})
