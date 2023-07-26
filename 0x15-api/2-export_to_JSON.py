#!/usr/bin/python3
"""
Function that exports data into a flatfile in
the JSON format
"""

if __name__ == "__main__":
    import json
    import requests as rq
    import sys

    uid = sys.argv[1]
    user = rq.get("https://jsonplaceholder.typicode.com/users/{}".format(uid))
    todos = rq.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    todoUser = {}
    taskList = []

    for task in todos:
        if task.get('userId') == int(uid):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            taskList.append(taskDict)
    todoUser[uid] = taskList

    fn = uid + '.json'
    with open(fn, mode='w') as f:
        json.dump(todoUser, f)
