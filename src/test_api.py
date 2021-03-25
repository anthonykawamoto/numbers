import json
from unittest.mock import patch

import pytest

from api import handler

valid_test_cases = [
    [{'queryStringParameters': {'id': '123'}}, {'statusCode': 200, 'body': json.dumps({'reversed': '321'})}, '321'],
    [{'queryStringParameters': {'id': '1'}}, {'statusCode': 200, 'body': json.dumps({'reversed': '1'})}, '1'],
]


@pytest.mark.parametrize('event, expected_response, reversed_value', valid_test_cases)
def test_returns_valid_responses(event, expected_response, reversed_value):
    with patch('db.table.get_item', return_value={'Item': {'reversed': reversed_value}}):
        assert handler(event, None) == expected_response


def test_nonexistent_id():
    test_event = {'queryStringParameters': {'id': 'doesnotexistid'}}

    with patch('db.table.get_item', return_value={}):
        assert handler(test_event, None) == {'statusCode': 200, 'body': json.dumps({})}


invalid_value_test_cases = [
    [{}, {'statusCode': 400}],
    [{'queryStringParameters': {'name': 'ted'}}, {'statusCode': 400}]
]


@pytest.mark.parametrize('event, expected_response', invalid_value_test_cases)
def test_returns_bad_request(event, expected_response):
    assert handler(event, None) == expected_response
