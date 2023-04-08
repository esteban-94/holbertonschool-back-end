#!/usr/bin/python3
"""Module"""

import json
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = user_url + "/todos/"

    user_info = requests.request('GET', user_url).json()
    todos_info = requests.request('GET', todos_url).json()

    with open('{}.json'.format(user_id), 'w') as jsonfile:
        json.dump({user_id: [{"task": task["title"],
                              "completed": task["completed"],
                              "username": user_info["username"]}
                             for task in todos_info]}, jsonfile)
