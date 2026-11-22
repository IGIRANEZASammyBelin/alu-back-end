# api

Python scripts that use a REST API to gather data about employees and
their TODO lists.

## Requirements

- Ubuntu 14.04 LTS, Python 3.4.3
- PEP 8 style, `requests` module

## Tasks

- `0-gather_data_from_an_API.py`: takes an employee ID and prints their
  TODO list progress.

## Usage

    ./0-gather_data_from_an_API.py 2
- `1-export_to_CSV.py`: takes an employee ID and exports all of their
  tasks to `USER_ID.csv`.
- `2-export_to_JSON.py`: takes an employee ID and exports all of their
  tasks to `USER_ID.json`.
- `3-dictionary_of_list_of_dictionaries.py`: exports the tasks of all
  employees to `todo_all_employees.json`.
