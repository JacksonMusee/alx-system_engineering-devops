#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]

    todos_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'

    todos = requests.get(todos_url).json()

    user_info = requests.get(user_url).json()
    user_name = user_info.get('username')

    new_todos_lst = []
    fieldnames = ["task", "completed", "username"]

    for item in todos:
        item["username"] = user_name
        item['task'] = item.get('title')
        tmpdict = {}
        for field in fieldnames:
            tmpdict[field] = item.get(field)
        new_todos_lst.append(tmpdict)

    final_data = {user_id: new_todos_lst}

    file_name = f"{user_id}.json"

    with open(file_name, 'w') as f:
        json.dump(final_data, f)

    f.close()
