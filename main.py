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
        add(args.filename, args.description, args.priority, args.est_dur, args.real_dur)
    if args.type == "modify":  
        modify(args.filename, int(args.id), args.description,args.priority, args.est_dur, args.real_dur)
    if args.type == "rm":  
        rm(args.filename, int(args.id))
    if args.type == "show":  
        show(args.filename)
    if args.type == "invoke_meta":
        add_meta_tache(args.filename, args.metataches_filename, args.id_meta, args.description,args.priority, args.est_dur, args.real_dur)


def add(filename, description, priorite, est_dur, real_dur):
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
        file.write(str(id_max+1) + ";" + description + ";" + str(priorite) +";"+ est_dur +";"+ real_dur +  "\n")

def add_meta_tache(tache_file,meta_tache_file,id,description,priorite,est_dur,real_dur):
    """
    Rajoute une tache qui existe déjà dans le fichier meta_tache_file au fichier tache_fil

    param str tache_file: le nom du fichier dans lequel on insère les taches
    param str meta_tache_file : le nom du fichier contenant les meta taches
    param int id : l'indice de la meta tache à insérer dans le fichier tache_file
    param str description : la nouvelle description de la tache dans tache_file(optionnel)
    param str description : la nouvelle description de la tache dans tache_file(optionnel)
    param int priorite : la nouvelle priorité de la tache dans tache_file(optionnel)
    param int est_dur : la nouvelle durée estimé de la tache dans tache_file(optionnel)
    param int real_dur : la nouvelle durée réelle de la tache dans tache_file(optionnel)
    
    """
    meta_lines=[]
    with open(meta_tache_file,'r') as f :
        meta_lines=f.readlines()
    not_found=True
    for line in meta_lines:
        info=get_infos(line)
        if info[0]==id:
            not_found=False
            des=info[1]
            prio=info[2]
            dur_est=info[3]
            dur_real=info[4]
            if description!=None:
                des=description
            if priorite!=None:
                prio=priorite
            if est_dur!=None:
                dur_est=est_dur
            if real_dur!=None:
                dur_real=real_dur
            add(tache_file, des, prio, dur_est, dur_real)
    if not_found:
        print("Not found this task in Meta_Task file")

def modify(filename, id, description, priority, est_dur, real_dur):
    """
    Modifie la tâche d'id _id_ avec la nouvelle description _description_ dans le fichier _filename_

    :param str filename: le nom du fichier a modifier
    :param str id: l'id de la tâche a modifier
    :param str description: la nouvelle description
    :param int priority: la priorité de la tâches
    :param int est_dur: la durée estimée de la tâche
    :param int real_dur: la durée réel de la tâche
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
                estdur=infos[3]
                realdur=infos[4]
                if description != None:
                    des = description
                if priority != None:
                    prio = priority
                if est_dur != None:
                    estdur= est_dur
                if real_dur != None:
                    realdur= real_dur
                file.write(str(id) + ";" + des + ";" + str(prio) + ";"+ str(estdur) + ";" + str(realdur) + "\n")
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

def filtrage(lines, f_description, f_motif, f_priorite):
    pass

def show(filename):
    """
    Affiche les informations du fichier _filename_

    :param str filename: le nom du fichier a afficher
    """
    
    lines = []
    lines_infos=[]
    with open(filename, 'r') as file:
        lines = file.readlines()
    max_len_infos = []
    for line in lines:
        infos = get_infos(line)
        lines_infos.append(infos)
        if not(max_len_infos):
            max_len_infos = [len(info) for info in infos]
        else:
            for i in range(len(infos)):
                max_len_infos[i] = max(max_len_infos[i], len(infos[i]))
    
    infos_case_size = []
    for _max in max_len_infos:
        infos_case_size.append(_max+2)

    separator = "+"
    for size in infos_case_size:
        separator += "".join(['-' for i in range(size)])+"+"

    print(separator)

    for infos in lines_infos:
        for i in range(len(infos)):
            print("|" , end="")
            print(" " + infos[i] + "".join([' ' for i in range(max_len_infos[i] - len(infos[i]) + 1)]), end="")
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
    parser_add.add_argument("priority", type=int, help="La priorite de la nouvelle tâche")
    parser_add.add_argument("est_dur", help="La duree estimee de la nouvelle tâche")
    parser_add.add_argument("real_dur", help="La duree realisee de la nouvelle tâche")

    #subparser for the invoke meta method
    parser_invoke_meta = subparsers.add_parser("invoke_meta", help="Ajouter une une tache qui copie une meta tâche")
    parser_invoke_meta.add_argument("metataches_filename", help="Le fichier des metas taches")
    parser_invoke_meta.add_argument("id_meta", help="L'id de la meta tache")
    parser_invoke_meta.add_argument("--d", dest="description", help="Une description imposée")
    parser_invoke_meta.add_argument("--p", type=int, dest="priority", help="Une priorité imposée")
    parser_invoke_meta.add_argument("--de", dest="est_dur", help="Une durée estimée imposée")
    parser_invoke_meta.add_argument("--dr", dest="real_dur", help="Une durée réalisée imposée")

    #subparser for the modify method
    parser_modify = subparsers.add_parser("modify", help="Modifier une tâche")
    parser_modify.add_argument("id", help="L'id de la tâche a modifier")
    parser_modify.add_argument("--d", dest="description", help="La description de la tâche a modifier")
    parser_modify.add_argument("--p", type=int, dest="priority", help="La priorité de la tâche a modifier")
    parser_modify.add_argument("--de", dest="est_dur", help="La durée estimée de la tâche a modifier")
    parser_modify.add_argument("--dr", dest="real_dur", help="La durée réalisée de la tâche a modifier")

    #subparser for the rm method
    parser_rm = subparsers.add_parser("rm", help="Supprimer une tâche")
    parser_rm.add_argument("id",help="L'id de la tâche a supprimer")

    #subparser for the show method
    parser_show = subparsers.add_parser("show", help="Afficher les tâches")
    parser_show.add_argument("-fm", dest="filtrage_motif",help="Filtre les tâches contenant le motif dans leur description")

    args = parser.parse_args()

    perform_action(args)

parse_performe()
