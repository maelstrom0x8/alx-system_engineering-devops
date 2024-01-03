#!/usr/bin/python3

"""
This script fetches user TODO information and exports the data
in the JSON format.
"""

import json
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
    url = "{}/todos?userId={}".format(BASE_URL, user_id)
    response = requests.get(url)
    return response.json()


if __name__ == '__main__':
    emp_id = sys.argv[1]
    usr = fetch_single_user(emp_id)
    todos = fetch_todos(usr.get('id'))
    lines = []

    for todo in todos:
        d = {
            'task': todo.get('title'), 'completed': todo.get('completed'),
            'username': usr.get('username')
        }

        lines.append(d)
    data = {usr.get('id'): lines}

    filename = "{}.json".format(emp_id)
    with open(filename, mode='w') as f:
        json.dump(data, f)
