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
    assert resp.status_code == 200, compose_response_msg(resp)
    post_resp_json = resp.json()

    resp = client.get_all_tasks()
    get_resp_json = resp.json()
    assert post_resp_json in get_resp_json

