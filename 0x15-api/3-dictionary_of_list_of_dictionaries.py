#!/usr/bin/python3

"""
This scripts fetches all users TODO information and
exports them to a JSON file
"""

import json
import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'


def fetch_all_users():
    """Fetch all users"""
    url = "{}/users".format(BASE_URL)
    users = requests.get(url)
    return users.json()


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
    users = fetch_all_users()
    lines = []
    data = {}

    for u in users:
        t = fetch_todos(u.get('id'))
        ln = []
        for g in t:
            d = {
                'username': u.get('username'), 'task': g.get('title'),
                'completed': g.get('completed')
            }
            ln.append(d)
        data[u.get('id')] = ln

    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as f:
        json.dump(data, f)
