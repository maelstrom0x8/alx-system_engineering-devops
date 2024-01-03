#!/usr/bin/python3

"""
This script fetches user TODO information and exports the data
in the CSV format.
"""

import requests
import sys

BASE_URL = 'https://jsonplaceholder.typicode.com'


def fetch_single_user(id: str):
    """Fetch a user"""
    url = "{}/users/{}".format(BASE_URL, id)
    usr = requests.get(url)
    return usr.json()


def fetch_todos(user_id: str):
    """Fetch all user todos"""
    url = "{}/todos?userId={}".format(BASE_URL, emp_id)
    response = requests.get(url)
    return response.json()


if __name__ == '__main__':
    emp_id = sys.argv[1]
    usr = fetch_single_user(emp_id)
    todos = fetch_todos(usr.get('id'))
    lines = []

    for todo in todos:
        fmt = "\"{}\",\"{}\",\"{}\",\"{}\""
        line = fmt.format(todo.get('userId'), usr.get('username'),
                          str(todo.get('completed')), todo.get('title'))
        lines.append(line + "\n")

    filename = "{}.csv".format(emp_id)
    with open(filename, mode='w') as f:
        f.writelines(lines)
