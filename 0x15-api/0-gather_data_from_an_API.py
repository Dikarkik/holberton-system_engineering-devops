#!/usr/bin/python3
"""
For a given employee ID,
returns information about his/her TODO list progress.
API: https://jsonplaceholder.typicode.com/users/1/todos
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    if len(sys.argv) < 2:
        sys.exit()

    url = 'https://jsonplaceholder.typicode.com/users/'
    data = json.loads(requests.get(url + sys.argv[1]).text)
    if not data:
        sys.exit()

    name = data.get('name')
    data = json.loads(requests.get(url + sys.argv[1] + '/todos').text)
    todo_done = 0

    for todo_task in data:
        if todo_task.get('completed') is True:
            todo_done += 1

    print('Employee' + name + 'is done with tasks({}/{}):'
          .format(todo_done, len(data)))

    for todo_task in data:
        if todo_task.get('completed') is True:
            print('\t ' + todo_task.get('title'))
