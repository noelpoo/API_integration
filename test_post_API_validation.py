from Common import *
from serverapi import ServerApi
from util import generate_random_string

invalid_email = '{}'.format(generate_random_string(3))
short_desc = generate_random_string(40)
long_desc = generate_random_string(500) + ' ' + generate_random_string(100)
invalid_date_string = '2020-1-1'
invalid_email_syntax = "abc.com@nodomain"


# TEST - missing field in payload should not return 200
def test_post_task_missing_field():
    assignee_email = ASSIGNEE
    reporter_email = REPORTER
    description = DESCRIPTION
    client = ServerApi(API_URL)

    resp = client.post_tasks_missing_field(assignee=assignee_email,
                                           reporter=reporter_email,
                                           description=description)
    assert resp.status_code != 200


# TEST - invalid assignee email in payload should not return 200
def test_post_task_invalid_assignee():
    assignee_email = invalid_email
    reporter_email = REPORTER
    description = DESCRIPTION
    duedate = DUEDATE
    client = ServerApi(API_URL)

    resp = client.post_tasks(assignee=assignee_email,
                             reporter=reporter_email,
                             description=description,
                             duedate=duedate)
    assert resp.status_code != 200


# TEST - invalid reporter email in payload should not return 200
def test_post_task_invalid_reporter():
    assignee_email = ASSIGNEE
    reporter_email = invalid_email
    description = DESCRIPTION
    duedate = DUEDATE
    client = ServerApi(API_URL)

    resp = client.post_tasks(assignee=assignee_email,
                             reporter=reporter_email,
                             description=description,
                             duedate=duedate)
    assert resp.status_code != 200


# TEST - invalid assignee email syntax in payload should not return 200
def test_post_task_invalid_assignee_syntax():
    assingee = invalid_email_syntax
    reporter = REPORTER
    description = DESCRIPTION
    duedate = DUEDATE

    client = ServerApi(API_URL)

    resp = client.post_tasks(assignee=assingee,
                             reporter=reporter,
                             description=description,
                             duedate=duedate)
    assert resp.status_code != 200


# TEST - invalid reporter email syntax in payload should not return 200
def test_post_task_invalid_reporter_syntax():
    assignee = ASSIGNEE
    reporter = invalid_email_syntax
    description = DESCRIPTION
    duedate = DUEDATE

    client = ServerApi(API_URL)

    resp = client.post_tasks(assignee=assignee,
                             reporter=reporter,
                             description=description,
                             duedate=duedate)
    assert resp.status_code != 200


# TEST - short description should not return 200
def test_post_task_short_description():
    assignee_email = ASSIGNEE
    reporter_email = REPORTER
    duedate = DUEDATE
    client = ServerApi(API_URL)

    resp = client.post_tasks(assignee=assignee_email,
                             reporter=reporter_email,
                             description=short_desc,
                             duedate=duedate)
    assert resp.status_code != 200


# TEST - long description should not return 200
def test_post_task_long_description():
    assignee_email = ASSIGNEE
    reporter_email = REPORTER
    duedate = DUEDATE
    client = ServerApi(API_URL)
    resp = client.post_tasks(assignee=assignee_email,
                             reporter=reporter_email,
                             description=long_desc,
                             duedate=duedate)
    assert resp.status_code != 200


# TEST - invalid date string format should not return 200
def test_post_task_invalid_date_string():
    assignee_email = ASSIGNEE
    reporter_email = REPORTER
    description = DESCRIPTION
    duedate = invalid_date_string
    client = ServerApi(API_URL)
    resp = client.post_tasks(assignee=assignee_email,
                             reporter=reporter_email,
                             description=description,
                             duedate=duedate)
    assert resp.status_code != 200

