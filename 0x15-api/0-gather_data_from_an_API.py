#!/usr/bin/python3

"""
0-gather_data_from_an_API.py

This script interacts with an API to fetch information about a user and their associated tasks.

Usage:
    python 0-gather_data_from_an_API.py <user_id>

Arguments:
    <user_id> (str): The ID of the user for whom to retrieve information.

The script performs the following tasks:
1. Fetches information about a user from the API.
2. Fetches all todos associated with the user.
3. Calculates the number of completed and total todos.
4. Prints a summary of the user's tasks.

Module Functions:
    - fetch_single_user(user_id: str) -> dict:
        Fetches information about a user from the API.

    - fetch_todos(user_id: str) -> list:
        Fetches all todos associated with a user from the API.

    - todos_stat(todos: list[dict]) -> tuple:
        Calculates the number of completed and total todos.

Script Execution:
    When executed as the main script:
    - Takes a user ID as a command-line argument.
    - Fetches user information and todos.
    - Calculates and prints the summary of completed and total todos.

Example:
    python 0-gather_data_from_an_API.py 1
"""


import requests
import sys

BASE_URL = 'https://jsonplaceholder.typicode.com'


def fetch_single_user(id: str):
    """
    Fetch information about a user from the API.

    Args:
        user_id (str): The ID of the user.

    Returns:
        dict: A dictionary containing user information.
    """
    url = "{}/users/{}".format(BASE_URL, id)
    usr = requests.get(url)
    return usr.json()


def fetch_todos(user_id: str):
    """
    Fetch all todos associated with a user from the API.

    Args:
        user_id (str): The ID of the user.

    Returns:
        list: A list of dictionaries representing todos.
    """
    url = "{}/todos?userId={}".format(BASE_URL, user_id)
    response = requests.get(url)
    return response.json()


def todos_stat(todos: list[dict]):
    """
    Calculate the number of completed and total todos.

    Args:
        todos (list[dict]): List of dictionaries representing todos.

    Returns:
        tuple: A tuple containing the number of completed and total todos.
    """
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
