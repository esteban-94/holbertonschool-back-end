#!/usr/bin/python3
"""Module"""

import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = user_url + "/todos/"

    user_info = requests.request('GET', user_url).json()
    todos_info = requests.request('GET', todos_url).json()

    emp_name = user_info["name"]
    task_completed = list(filter(lambda obj:
                                 (obj["completed"] is True), todos_info))
    number_tasks = len(task_completed)
    total_tasks = len(todos_info)

    print("Employee {} is done with tasks({}/{}):".
          format(emp_name, number_tasks, total_tasks))

    [print("\t " + task["title"]) for task in task_completed]
