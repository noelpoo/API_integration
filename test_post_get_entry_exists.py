from Common import *
from serverapi import ServerApi
from util import compose_response_msg, generate_random_string, generate_random_date


def test_post_entry_exists():
    assignee_email = '{}@nodomain.com'.format(generate_random_string(3))
    reporter_email = '{}@nodomain.com'.format(generate_random_string(3))
    description = DESCRIPTION
    duedate = generate_random_date()

    client = ServerApi(api_url=API_URL)
    resp = client.post_tasks(assignee=assignee_email,
                             reporter=reporter_email,
                             description=description,
                             duedate=duedate)
    # TEST - post request is successful
    assert resp.status_code == 200, compose_response_msg(resp)
    post_resp_json = resp.json()

    returned_assignee = post_resp_json.get('assignee', '')
    returned_reporter = post_resp_json.get('reporter', '')
    returned_duedate = post_resp_json.get('dueDate', '')
    # TEST - post response field matches request fields
    assert returned_reporter == reporter_email \
           and returned_assignee == assignee_email \
           and returned_duedate == duedate
    # TEST - check if posted entry exists in task list
    # TODO - add a timeout/sleep logic to account for DB sync delay
    resp = client.get_all_tasks()
    get_resp_json = resp.json()
    assert post_resp_json in get_resp_json

