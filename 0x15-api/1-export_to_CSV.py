#!/usr/bin/python3
"""
This is a function that exports data from an API to
a flat file in csv format
"""

if __name__ == "__main__":

    import csv
    import requests as rq
    import sys

    uid = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/users"
    user = rq.get("{}/{}".format(url, str(uid)))
    name = user.json().get('username')
    todos = rq.get('{}/{}/todos'.format(url, str(uid)))
    tasks = todos.json()
    fn = '{}.csv'.format(str(uid))

    with open(fn, mode='w') as f:
        for task in tasks:
            f.write('"{}","{}","{}","{}"\n'
                    .format(uid, name, task.get('completed'),
                            task.get('title')))
