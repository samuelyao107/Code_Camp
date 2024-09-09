# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import argparse






# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Une fonction qui récupère la liste des tâches avec leurs ids
def load_tasks(filename):
    tasks = {}
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(' ', 1)
                if len(parts) == 2:
                    task_id, description = parts
                    tasks[int(task_id)] = description
    return tasks

# Fonction pour sauvegarder les tâches dans un fichier texte
def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task_id, description in sorted(tasks.items()):
            file.write(f"{task_id} {description}\n")

def modify_task(filename, task_id, new_description):
    tasks = load_tasks(filename)
    if task_id in tasks:
        tasks[task_id] = new_description
        save_tasks(filename, tasks)
        print(f"Tâche {task_id} modifiée.")
    else:
        print(f"Erreur : la tâche avec l'ID {task_id} n'a pas été trouvée.")

def modify_parser():
    parser = argparse.ArgumentParser(description="Gestionnaire de tâches")
    parser.add_argument("filename", help="Nom du fichier contenant les tâches")

    subparsers = parser.add_subparsers(dest="command")

    modify_parser = subparsers.add_parser("modify", help="Modifier une tâche existante")
    modify_parser.add_argument("id", type=int, help="ID de la tâche à modifier")
    modify_parser.add_argument("description", help="Nouvelle description de la tâche", nargs='+')

    args = parser.parse_args()


    # Traitement des commandes
    if  args.command == "modify":
        modify_task(args.filename, args.id, ' '.join(args.description))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    modify_parser()

