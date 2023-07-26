#!/usr/bin/python3
"""
A function that displays a list of TODO for a given employee
with the employee ID specified
"""


if __name__ == "__main__":
    import requests as rq
    import sys

    uid = int(sys.argv[1])
    baseUrl = "https://jsonplaceholder.typicode.com/"
    url = baseUrl + "users/" + str(uid)

    response = rq.get(url)
    name = response.json().get('name')

    todoUrl = url + "/todos"
    response = rq.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed') is True:
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
