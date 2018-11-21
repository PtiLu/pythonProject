# Modèle du niveau 1
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

# Affiche un labyrinthe passé en entrée
def affiche_labyrinthe (lab):
    for ligne in lab:
        print(ligne)

# Construit un labyrinthe custom à base de la taille passée en entrée
def affiche_bordure_labyrinthe(taille):
    longueur=(taille-2)*2
    print("La longueur = ",longueur)
    print("+{}+".format("-" * (longueur-2)))
    for i in range(taille - 2):
        print("|{}|".format(" " * (longueur-2)))
    print("+{}+".format("-" * (longueur-2)))

# ---------------------Début du script-----------------------
choix = int(input("Quelle type de labyrinthe voulez vous afficher?\nPar défaut:1\nCustom:2\nChoix : "))
if choix == 1:
    val_retour = affiche_labyrinthe(level_1)
    print("Code retour = ",val_retour,sep="")
else:
    taille=int(input("Entrez la longueur des côtés du labyrinthe: "))
    affiche_bordure_labyrinthe(taille)