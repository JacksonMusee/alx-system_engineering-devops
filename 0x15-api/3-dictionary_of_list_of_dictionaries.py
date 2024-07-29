#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

import copy
import json
import requests


if __name__ == "__main__":
    todos_url = f'https://jsonplaceholder.typicode.com/todos'
    users_url = f'https://jsonplaceholder.typicode.com/users'

    todos = requests.get(todos_url).json()
    users = requests.get(users_url).json()

    alluser_todo_dict = {}
    fieldnames = ["username", "task", "completed"]

    for user in users:
        tmplst = []
        for todo in todos:
            if todo.get('userId') == user.get('id'):
                todo['username'] = user.get('username')
                todo['task'] = todo.get('title')
                tmpdict = {}
                for field in fieldnames:
                    tmpdict[field] = todo.get(field)
                tmplst.append(tmpdict.copy())
                del tmpdict
        alluser_todo_dict[user.get('id')] = tmplst[:]
        del tmplst

    file_name = "todo_all_employees.json"

    with open(file_name, 'w') as f:
        json.dump(alluser_todo_dict, f)

    f.close()
