#Jeronimo gomez et Daoud Hechaichi
#17/10/2025
#but: créer le jeu du casse briques en tkinter 
#à améliorer: rajouter la possibilité de changer les toucher, et jouer ave la souris


from tkinter import Tk
from jeu import jeu



def centrer_fenetre(fenetre, longueur_fenetre, largeur_fenetre):
    """
    # fonction pour centrer la fenetre dans l'ecran
    # Entrées: fenetre, longueur de la fenetre(enntier), largeur de la fenetre(entier)
    # Sorties: chaine de caracteres avec la geometrie de la fenetre, a inserer dans fenetre.geometry()
    """   
    longueur_ecran= fenetre.winfo_screenwidth() #recupere la largeur de l'ecran
    largeur_ecran= fenetre.winfo_screenheight() #recupere la hauteur de l'ecran

    x= (longueur_ecran - longueur_fenetre)//2 #calcule la position x pour centrer la fenetre en longueur
    y= (largeur_ecran - largeur_fenetre)//2   #calcule la position y pour centrer la fenetre en largeur
    
    return f"{longueur_fenetre}x{largeur_fenetre}+{x}+{y}"


# Programme principal
# Initialisation de la fenetre principale, titre, dimensions et couleur de fond 
MaFenetre = Tk()
MaFenetre.title("Jeu du casse-briques")
MaFenetre.geometry(centrer_fenetre(MaFenetre, 1000,600))
MaFenetre.config(bg="gray20")

#jeu: canvas et frames
jeu(MaFenetre)

# Actualisation de la fenetre
MaFenetre.mainloop()

