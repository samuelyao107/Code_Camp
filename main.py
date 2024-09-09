# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    rm("taches.txt",4)
    print("modified")




       


