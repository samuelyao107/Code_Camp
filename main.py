import argparse
import os


def rm(fichier_name,id):
    
    lignes_mofifies=[]
    
    with open(fichier_name, 'r') as f:
        lignes = f.readlines()
        
    for ligne in lignes:
            #index+=1
            partie_gauche, partie_droite = ligne.split(';', 1)
            if partie_gauche!=id:
                 lignes_mofifies.append(ligne)

    with open(fichier_name,'w') as f:
         f.writelines(lignes_mofifies)   
            
    print("ligne removed?")

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

def modify_task(file_name, task_id, new_description):
    # Lire les tâches existantes à partir du fichier
    tasks = read_tasks(file_name)
    
    # Chercher la tâche avec l'ID donné
    for i, task in enumerate(tasks):
        if task[0] == task_id:  # Comparer l'ID de la tâche
            tasks[i] = (task_id, new_description)  # Modifier la description
            write_tasks(file_name, tasks)  # Écrire les tâches mises à jour dans le fichier
            print(f"Tâche {task_id} modifiée.")
            return
    
    # Si la tâche avec l'ID donné n'a pas été trouvée
    print(f"Erreur : la tâche avec l'ID {task_id} n'a pas été trouvée.")

def main():
    parser = argparse.ArgumentParser(description='Simple Task Management System')
    parser.add_argument('filename', help='Name of the file where tasks are stored')

    subparsers = parser.add_subparsers(dest='command', required=True)

    # Subparser for the "add" command
    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('description', nargs='+', help='Description of the task')

    # Subparser for the "add" command
    modify_parser = subparsers.add_parser("modify", help="Modifier une tâche existante")
    modify_parser.add_argument("id", type=int, help="ID de la tâche à modifier")
    modify_parser.add_argument("description", help="Nouvelle description de la tâche", nargs='+')

    args = parser.parse_args()

    if args.command == 'add':
        description = " ".join(args.description)
        add_task(args.filename, description)
    elif args.command == 'modify':
        modify_task(args.filename, args.id, ' '.join(args.description))

if __name__ == "__main__":
    main()

