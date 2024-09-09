import argparse
import os


def read_tasks(file_name):
    if not os.path.exists(file_name):
        return []
    with open(file_name, 'r') as f:
        lines = f.readlines()
    tasks = [line.strip().split(",", 1) for line in lines if line.strip()]
    return [(int(task[0]), task[1]) for task in tasks]

def write_tasks(file_name, tasks):
    with open(file_name, 'w') as f:
        for task in tasks:
            f.write(f"{task[0]},{task[1]}\n")

def add_task(file_name, description):
    tasks = read_tasks(file_name)
    new_id = max([task[0] for task in tasks], default=0) + 1
    tasks.append((new_id, description))
    write_tasks(file_name, tasks)
    print(f"Added task with ID: {new_id}")

def main():
    parser = argparse.ArgumentParser(description='Simple Task Management System')
    parser.add_argument('filename', help='Name of the file where tasks are stored')

    subparsers = parser.add_subparsers(dest='command', required=True)

    # Subparser for the "add" command
    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('description', nargs='+', help='Description of the task')

    args = parser.parse_args()

    if args.command == 'add':
        description = " ".join(args.description)
        add_task(args.filename, description)

if __name__ == "__main__":
    main()