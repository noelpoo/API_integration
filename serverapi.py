import requests


class ServerApi:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_all_tasks(self):
        api_url = self.api_url
        payload = ''
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        return requests.get(api_url, json=payload, headers=headers, verify=False)

    def post_tasks(self, assignee, reporter, description, duedate):
        api_url = self.api_url
        payload = {
            "assignee": str(assignee),
            "reporter": str(reporter),
            "description": str(description),
            "dueDate": str(duedate)
        }
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        return requests.post(api_url, json=payload, headers=headers, verify=False)

    def get_task_id(self, id):
        api_url = '{}/{}'.format(self.api_url, id)
        payload = ''
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache"
        }
        return requests.get(api_url, json=payload, headers=headers, verify=False)

    def post_tasks_missing_field(self, assignee, reporter, description):
        api_url = self.api_url
        payload = {
            "assignee": str(assignee),
            "reporter": str(reporter),
            "description": str(description),
        }
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        return requests.post(api_url, json=payload, headers=headers, verify=False)





