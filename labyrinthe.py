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

# Déclaration du personnage et de sa position initiale
perso = "X"
pos_perso = [1, 1]

def affiche_labyrinthe (lab):
    """
        Affichage d'un labyrinthe

        lab: Variable contenant le labyrinthe
    """
    nb_ligne=0
    for ligne in lab:
        print(ligne)
        nb_ligne++
        
def affiche_bordure_labyrinthe(taille):
    """
        Construit un labyrinthe custom

        taille: Variable contenant la taille (longueur et largeur) du labyrinthe
    """
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