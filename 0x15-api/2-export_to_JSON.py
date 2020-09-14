#!/usr/bin/python3
"""
Export data in the JSON format.
For a given employee ID,
records all tasks that are owned by this employee.

Format must be:
{ "USER_ID": [ {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}}, {"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, ... ]}

File name must be: USER_ID.json
API: https://jsonplaceholder.typicode.com/users/1/todos
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    if len(sys.argv) < 2:
        sys.exit()

    url = 'https://jsonplaceholder.typicode.com/users/'
    id = sys.argv[1]
    data = json.loads(requests.get(url + id).text)
    if not data:
        sys.exit()

    username = data.get('username')
    data = json.loads(requests.get(url + id + '/todos').text)

    tasks = []

    for todo_task in data:
        tasks.append({'task': todo_task.get('title'),
                      'completed': todo_task.get('completed'),
                      'username': username})

    with open('{}.json'.format(id), mode='w', encoding='utf-8') as file:
        json.dump({'{}'.format(id): tasks}, file)
