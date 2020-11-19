from serverapi import ServerApi
from Common import *
from util import json_schema_check

api_url = API_URL
schema = GET_TASK_SCHEMA


def test_post_tasks():
    client = ServerApi(api_url=API_URL)
    resp = client.get_all_tasks()
    json_schema_check(resp, schema, expected_status=200)