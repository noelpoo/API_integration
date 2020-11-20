from Common import *
from serverapi import ServerApi
from util import compose_response_msg


def test_get_task_id_not_exist():
    client = ServerApi(API_URL)
    resp = client.get_all_tasks()
    # TEST - get all task success
    assert resp.status_code == 200, compose_response_msg(resp)
    resp_json = resp.json()

    task_ids = []
    for task in resp_json:
        task_id = task.get('taskId')
        task_ids.append(task_id)

    latest_id = max(task_ids)

    # TEST - querying a non-existent id should return 404
    resp = client.get_task_id(id=latest_id + 1)
    assert resp.status_code == 404, 'should return 404, as task_id should not exist'

