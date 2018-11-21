level_1 = [ 
    "+----------------------------+",
    "|                            |",
    "|                            |",
    "|                            |",
    "|                            |",
    "|                            |",
    "|                            |",
    "|                            |",
    "|                            |",
    "|                            |",
    "|                            |",
    "|                            |",
    "|                            |",
    "|                            |",
    "|                            |",
    "|                            |",
    "|                            |",
    "|                            |",
    "|                            |",
    "+----------------------------+"  
]

def affiche_labyrinthe (lab):
    for ligne in lab:
        print(ligne)

val_retour = affiche_labyrinthe(level_1)
print("Code retour = ",val_retour,sep="")