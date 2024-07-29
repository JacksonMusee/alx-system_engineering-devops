#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

import requests
from sys import argv


if __name__ == "__main__":
    todos_url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'

    todos = requests.get(todos_url)

    user_info = requests.get(user_url)
    user_info_json = user_info.json()
    user_name = user_info_json.get('name')

    data = todos.json()
    completed_tasks = []
    for item in data:
        if item["completed"] is True:
            completed_tasks.append(item)

    out_part_1 = f"Employee {user_name} is done with"
    out_oart_2 = f"tasks({len(completed_tasks)}/{len(data)}):"
    print(out_part_1, out_oart_2)

    for item in completed_tasks:
        print(f'\t {item.get("title")}')
