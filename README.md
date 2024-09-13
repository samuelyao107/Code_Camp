
# Task Manager

## Description
Ce projet est un gestionnaire de tâches simple écrit en Python. Il permet d'ajouter, de modifier, de supprimer et d'afficher des tâches depuis un fichier texte. Il prend également en charge l'ajout de tâches à partir de "meta-tâches" stockées dans un autre fichier.

## Prérequis
Avant de commencer, assurez-vous d'avoir installé les éléments suivants :
- Python


## Utilisation
Le script main.py propose plusieurs commandes pour gérer des tâches à partir d'un fichier texte. Voici les commandes principales :

### Ajouter une tâche
```bash
python main.py <fichier> add <description> <priorité> <durée estimée> <durée réelle>
```

### Modifier une tâche
```bash
python main.py <fichier> modify <id_tâche> [--d <description>] [--p <priorité>] [--de <durée estimée>] [--dr <durée réelle>]
```

### Supprimer une tâche
```bash
python main.py <fichier> rm <id_tâche>
```

### Afficher les tâches
```bash
python main.py <fichier> show [-fm <motif>] [-fd <description>] [-fp <priorité>]
```

### Ajouter une "meta-tâche" à partir d'un autre fichier
```bash
python main.py <fichier_tâche> invoke_meta <fichier_meta> <id_meta> [--d <description>] [--p <priorité>] [--de <durée estimée>] [--dr <durée réelle>]
```

## Structure du projet
```
task-manager/
├── main.py       # Le script principal pour gérer les tâches
└── <fichiers>    # Fichiers de tâches à gérer
```

