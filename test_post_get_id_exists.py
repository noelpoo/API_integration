from Common import *
from serverapi import ServerApi
from util import compose_response_msg, generate_random_string, generate_random_date


def test_post_get_id_exists():
    assignee_email = '{}@nodomain.com'.format(generate_random_string(3))
    reporter_email = '{}@nodomain.com'.format(generate_random_string(3))
    description = DESCRIPTION
    duedate = generate_random_date()

    client = ServerApi(api_url=API_URL)
    resp = client.post_tasks(assignee=assignee_email,
                             reporter=reporter_email,
                             description=description,
                             duedate=duedate)
    # TEST - post task request is successful
    assert resp.status_code == 200, compose_response_msg(resp)
    resp_json = resp.json()
    expected_id = resp_json.get('taskId')

    # TEST - get task id request is successful
    resp = client.get_task_id(id=expected_id)
    assert resp.status_code == 200, compose_response_msg(resp)

    # TEST - returned fields matches post request fields
    resp_json = resp.json()
    returned_assignee = resp_json.get('assignee', '')
    returned_reporter = resp_json.get('reporter', '')
    returned_duedate = resp_json.get('dueDate', '')

    assert returned_assignee == assignee_email\
           and returned_reporter == reporter_email\
           and returned_duedate == duedate


