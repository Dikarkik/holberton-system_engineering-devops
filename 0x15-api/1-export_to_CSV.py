#!/usr/bin/python3
"""
Export data in the CSV format.
For a given employee ID,
records all tasks that are owned by this employee.
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
API: https://jsonplaceholder.typicode.com/users/1/todos
"""

if __name__ == "__main__":
    import csv
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

    with open('{}.cvs'.format(id), mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=",", quoting=csv.QUOTE_ALL)
        for task in data:
            writer.writerow([id, username, task.get('completed'),
                            task.get('title')])
