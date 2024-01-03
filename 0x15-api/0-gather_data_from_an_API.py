#!/usr/bin/python3

"""
This script fetches for a given employee ID, returns information
about his/her TODO list progress.
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
    url = "{}/todos?userId={}".format(BASE_URL, user_id)
    response = requests.get(url)
    return response.json()


def todos_stat(todos: list[dict]):
    """ From a collection of todos this function gets the
        number of todos and the completed ones"""
    total = 0
    completed = 0
    for e in todos:
        if e.get('completed'):
            completed += 1
        total += 1
    return completed, total


if __name__ == '__main__':
    emp_id = sys.argv[1]
    usr = fetch_single_user(emp_id)
    todos = fetch_todos(usr.get('id'))
    c, t = todos_stat(todos)
    print("Employee {} is done with tasks ({}/{})".format(
        usr.get('name'), c, t))
    [print("  {}".format(x.get('title'))) for x in todos]
