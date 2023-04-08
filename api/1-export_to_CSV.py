#!/usr/bin/python3
"""Module"""

import csv
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = user_url + "/todos/"

    user_info = requests.request('GET', user_url).json()
    todos_info = requests.request('GET', todos_url).json()

    with open('{}.csv'.format(user_id), 'w') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [csvwriter.writerow([user_id, user_info["username"],
                             task["completed"], task["title"]])
         for task in todos_info]
