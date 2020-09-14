#!/usr/bin/python3
"""
Export data in the JSON format.
Records all tasks from all employees.

Format must be:
{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ],
"USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}

File name must be: todo_all_employees.json
API: https://jsonplaceholder.typicode.com/users/1/todos
"""

if __name__ == "__main__":
    import json
    import requests

    tasks_all_employees = {}

    url = 'https://jsonplaceholder.typicode.com/users/'
    employees = json.loads(requests.get(url).text)

    for employee in employees:
        id = str(employee.get('id'))
        username = employee.get('username')
        data = json.loads(requests.get(url + id + '/todos').text)

        tasks = []
        for todo_task in data:
            tasks.append({'task': todo_task.get('title'),
                         'completed': todo_task.get('completed'),
                         'username': username})

        tasks_all_employees[id] = tasks

    with open('todo_all_employees.json', mode='w', encoding='utf-8') as file:
        json.dump(tasks_all_employees, file)
