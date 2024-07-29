#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

import csv
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
    fieldnames = ["userId", "username", "completed", "title"]

    for item in todos:
        item["username"] = user_name
        tmpdict = {}
        for field in fieldnames:
            tmpdict[field] = str(item.get(field))
        new_todos_lst.append(tmpdict)

    file_name = f"{user_id}.csv"

    with open(file_name, 'w') as f:
        my_writer = csv.DictWriter(f, fieldnames=fieldnames,
                                   quoting=csv.QUOTE_ALL)
        for item in new_todos_lst:
            print(item)
            my_writer.writerow(item)

    f.close()
