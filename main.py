import argparse as ap


def get_id(line):
    """
    Récupère l'id inscrite sur une ligne de tâche

    :param str line: La ligne dans laquelle il faut récupérer l'id

    :return: l'id récupéré
    :rtype: int
    """
    if line == "":
        return None
    id_str = ""
    i = 0
    while line[i] != ';':
        id_str += line[i]
        i += 1
    return int(id_str)

def get_infos(line):
    """
    Récupère les infos inscrites dans une ligne de tâche (séparées par ;)

    :param str line: La ligne dans laquelle il faut récupérer les infos

    :return: la liste des infos récup
    :rtype: list of string
    """
    res = []
    if line == "":
        return []
    str = ""
    for c in line:
        if c != ';' and c != '\n':
            str += c
        else:
            res.append(str)
            str = ""
    return res

def perform_action(args):
    """
    Exécute l'action demandée par la ligne de commande, laquelle est stockée dans args
    """
    if args.type == "add":
        add(args.filename, args.description, args.priorite)
    if args.type == "modify":  
        modify(args.filename, int(args.id), args.description,args.priority)
    if args.type == "rm":  
        rm(args.filename, int(args.id))
    if args.type == "show":  
        show(args.filename)


def add(filename, description, priorite):
    """
    Rajoute une nouvelle tâche de description _description_ dans le fichier _filename_ 

    :param str filename: le nom du fichier a modifier
    :param str description: la description de la nouvelle tâche
    """
    id_max = -1
    with open(filename, 'r') as file:
        lines = file.readlines()
        if len(lines) != 0:
            id_max = get_id(lines[-1])
    
    with open(filename, 'a') as file:
        file.write(str(id_max+1) + ";" + description + ";" + priorite + "\n")


def modify(filename, id, description, priority):
    """
    Modifie la tâche d'id _id_ avec la nouvelle description _description_ dans le fichier _filename_

    :param str filename: le nom du fichier a modifier
    :param str id: l'id de la tâche a modifier
    :param str description: la nouvelle description
    """
    lines = []
    notfound = True
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            if get_id(line) != id :
                file.write(line)
            else:
                infos = get_infos(line)
                des = infos[1]
                prio = infos[2]
                if description != None:
                    des = description
                if priority != None:
                    prio = priority
                file.write(str(id) + ";" + des + ";" + str(prio) +"\n")
                notfound = False
    if notfound :
        print("ERROR : id not found")

def rm(filename, id):
    """
    Enlève la tâche d'id _id_ dans le fichier _filename_

    :param str filename: le nom du fichier a modifier
    :param str id: l'id de la tâche a supprimer
    """
    lines = []
    notfound = True
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            if get_id(line) != id :
                file.write(line)
            else :
                notfound = False
    if notfound:
        print("ERROR : id not found")

def show(filename):
    """
    Modifie les tâches du fichier _filename_

    :param str filename: le nom du fichier a afficher
    """
    lines = []
    lines_infos=[]
    with open(filename, 'r') as file:
        lines = file.readlines()
    max_len_id = 0
    max_len_des = 0
    max_len_prio=0
    for line in lines:
        infos = get_infos(line)
        lines_infos.append(infos)
        max_len_id = max(max_len_id, len(infos[0]))
        max_len_des = max(max_len_des, len(infos[1]))
        max_len_prio=max(max_len_prio,len(infos[2]))
    id_case_size = max_len_id + 2
    des_case_size = max_len_des + 2
    prio_case_size=max_len_prio+2
    separator = "+" + "".join(['-' for i in range(id_case_size)]) + "+" + "".join(['-' for i in range(des_case_size)]) + "+"+"".join(['-' for i in range(prio_case_size) ])+"+"
    print(separator)

    for info in lines_infos:
        print("|" , end="")
        print(" " + info[0] + "".join([' ' for i in range(max_len_id - len(info[0]) + 1)]), end="")
        print("|", end="")
        print(" " + info[1] + "".join([' ' for i in range(max_len_des - len(info[1]) + 1)]), end="")
        print("|",end="")
        print( " " +info[2]+"".join([' ' for i in range(max_len_prio-len(info[2])+1)]),end="")
        print("|")
        print(separator)

def parse_performe():
    """
    Lit la ligne de commande et éxécute les opérations nécessaires.
    """
    parser = ap.ArgumentParser()
    parser.add_argument("filename", default="", help="le nom du fichier sur laquelle l'action est réalisée")
    subparsers = parser.add_subparsers(dest="type", help="le type d'action a effectuer")

    #subparser for the add method
    parser_add = subparsers.add_parser("add", help="Ajouter une tâche")
    parser_add.add_argument("description", help="La description de la nouvelle tâche")
    parser_add.add_argument("priority", help="La priorite de la nouvelle tâche")
    parser_add.add_argument("est_dur", help="La durée estimée de la nouvelle tâche")
    parser_add.add_argument("real_dur", help="La durée réalisée de la nouvelle tâche")

    #subparser for the modify method
    parser_modify = subparsers.add_parser("modify", help="Modifier une tâche")
    parser_modify.add_argument("id", help="L'id de la tâche a modifier")
    parser_modify.add_argument("--d", dest="description", help="La description de la tâche a modifier")
    parser_modify.add_argument("--p", dest="priority", help="La priorité de la tâche a modifier")
    parser_modify.add_argument("--de", dest="est_dur", help="La durée estimée de la tâche a modifier")
    parser_modify.add_argument("--dr", dest="real_dur", help="La durée réalisée de la tâche a modifier")

    #subparser for the rm method
    parser_rm = subparsers.add_parser("rm", help="Supprimer une tâche")
    parser_rm.add_argument("id",help="L'id de la tâche a supprimer")

    #subparser for the show method
    parser_show = subparsers.add_parser("show", help="Afficher les tâches")

    args = parser.parse_args()

    perform_action(args)

parse_performe()
