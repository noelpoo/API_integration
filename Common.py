# Constants
API_URL = 'http://localhost:9090/v1/tasks'

ASSIGNEE = "abc@noDomain.com"
REPORTER = "xyz@nodomain.com"
DESCRIPTION = "Please go through the API documentation and write the integration test for the APIs. Try to cover all possible scenarios.",
DUEDATE = "2020-11-30"

POST_TASK_SCHEMA = {
    "type": "object",
    "properties": {
        "taskId": {"type": "number"},
        "assignee": {"type": "string"},
        "reporter": {"type": "string"},
        "description": {"type": "string"},
        "dueDate": {"type": "string"}
    }
}

GET_TASK_SCHEMA = {
    "type": "array",
    "items": [
        {
            "type": "object",
            "properties": {
                "taskId": {"type": "number"},
                "assignee": {"type": "string"},
                "reporter": {"type": "string"},
                "description": {"type": "string"},
                "dueDate": {"type": "string"}
            }
        }
    ]
}

GET_TASK_ID_SCHEMA = POST_TASK_SCHEMA
