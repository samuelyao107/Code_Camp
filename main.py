import argparse
import os

# File structure: id,description
def read_tasks(file_name):
    if not os.path.exists(file_name):
        return []
    with open(file_name, 'r') as f:
        lines = f.readlines()
    tasks = [line.strip().split(";", 1) for line in lines if line.strip()]
    return [(int(task[0]), task[1]) for task in tasks]

def write_tasks(file_name, tasks):
    with open(file_name, 'w') as f:
        for task in tasks:
            f.write(f"{task[0]};{task[1]}\n")

def add_task(file_name, description):
    tasks = read_tasks(file_name)
    new_id = max([task[0] for task in tasks], default=0) + 1
    tasks.append((new_id, description))
    write_tasks(file_name, tasks)
    print(f"Added task with ID: {new_id}")

