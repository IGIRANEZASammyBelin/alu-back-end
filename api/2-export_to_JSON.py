#!/usr/bin/python3
"""Export an employee's TODO list data to a JSON file."""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos",
                         params={"userId": user_id}).json()

    tasks = [{"task": t.get("title"),
              "completed": t.get("completed"),
              "username": user.get("username")} for t in todos]

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: tasks}, jsonfile)
