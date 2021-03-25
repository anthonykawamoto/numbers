import json
import pytest
from api import handler

valid_test_cases = [
    [{'queryStringParameters': {'id': '123'}}, {'statusCode': 200, 'body': json.dumps({'message': '321'})}],
    [{'queryStringParameters': {'id': 'nonExistentId'}}, {'statusCode': 200, 'body': json.dumps({})}],
]


@pytest.mark.parametrize('event, expected_response', valid_test_cases)
def test_returns_valid_responses(event, expected_response):
    assert handler(event, None) == expected_response


invalid_value_test_cases = [
    [{}, {'statusCode': 400}],
    [{'queryStringParameters': {'name': 'ted'}}, {'statusCode': 400}]
]


@pytest.mark.parametrize('event, expected_response', invalid_value_test_cases)
def test_returns_bad_request(event, expected_response):
    assert handler(event, None) == expected_response
