from Common import *
from serverapi import ServerApi
from util import generate_random_string

invalid_email = '{}'.format(generate_random_string(3))
short_desc = generate_random_string(40)
long_desc = generate_random_string(500)


def test_post_task_missing_field():
    assignee_email = '{}@nodomain.com'.format(generate_random_string(3))
    reporter_email = '{}@nodomain.com'.format(generate_random_string(3))
    description = DESCRIPTION
    client = ServerApi(API_URL)

    resp = client.post_tasks_missing_field(assignee=assignee_email,
                                           reporter=reporter_email,
                                           description=description)
    assert resp.status_code != 200


def test_post_task_invalid_assignee():
    assignee_email = invalid_email
    reporter_email = '{}@nodomain.com'.format(generate_random_string(3))
    description = DESCRIPTION
    duedate = DUEDATE
    client = ServerApi(API_URL)

    resp = client.post_tasks(assignee=assignee_email,
                             reporter=reporter_email,
                             description=description,
                             duedate=duedate)
    assert resp.status_code != 200


def test_post_task_invalid_reporter():
    assignee_email = '{}@nodomain.com'.format(generate_random_string(3))
    reporter_email = invalid_email
    description = DESCRIPTION
    duedate = DUEDATE
    client = ServerApi(API_URL)

    resp = client.post_tasks(assignee=assignee_email,
                             reporter=reporter_email,
                             description=description,
                             duedate=duedate)
    assert resp.status_code != 200


def test_post_task_short_description():
    assignee_email = '{}@nodomain.com'.format(generate_random_string(3))
    reporter_email = '{}@nodomain.com'.format(generate_random_string(3))
    duedate = DUEDATE
    client = ServerApi(API_URL)

    resp = client.post_tasks(assignee=assignee_email,
                             reporter=reporter_email,
                             description=short_desc,
                             duedate=duedate)
    assert resp.status_code != 200


def test_post_task_long_description():
    assignee_email = '{}@nodomain.com'.format(generate_random_string(3))
    reporter_email = '{}@nodomain.com'.format(generate_random_string(3))
    duedate = DUEDATE
    client = ServerApi(API_URL)
    resp = client.post_tasks(assignee=assignee_email,
                             reporter=reporter_email,
                             description=long_desc,
                             duedate=duedate)
    assert resp.status_code != 200
