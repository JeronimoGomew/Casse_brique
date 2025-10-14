import tkinter as tk
import classes_balle as b
import Brique as br
import classe_plateforme as pl

# fonction pour centrer la fenetre dans l'ecran
# Entrées: fenetre, longueur de la fenetre(enntier), largeur de la fenetre(entier)
# Sorties: chaine de caracteres avec la geometrie de la fenetre, a inserer dans fenetre.geometry()

def centrer_fenetre(fenetre, longueur_fenetre, largeur_fenetre):
    
    longueur_ecran= fenetre.winfo_screenwidth() #recupere la largeur de l'ecran
    largeur_ecran= fenetre.winfo_screenheight() #recupere la hauteur de l'ecran

    x= (longueur_ecran - longueur_fenetre)//2 #calcule la position x pour centrer la fenetre en longueur
    y= (largeur_ecran - largeur_fenetre)//2   #calcule la position y pour centrer la fenetre en largeur
    
    return f"{longueur_fenetre}x{largeur_fenetre}+{x}+{y}"


# fonction pour demarrer une nouvelle partie
# Entrées: aucune
# Sorties: aucune
# elle se declenche quand on appuie sur le bouton demarrer une nouvelle partie
def demarrer():

    balle1.changer_vitesse(5)
    for i in range(9):
        liste_briques()[i]
    
    brique_test=br.Brique(Zone_jeu,9,60,90,40,"blue")
    balle1.mouvement(brique_test,plateforme)
    
    #balleinit.detruire()


def liste_briques():
    marge = 10
    liste_br = []

    for j in range (4):
        for i in range (10):
            brique=br.Brique(Zone_jeu,9 + i*90 + i*9,10 + 50*j,90,40,"blue")
            liste_br.append(brique)
    return liste_br
       














# Programme principal
# Initialisation de la fenetre principale, titre, dimensions et couleur de fond 
MaFenetre = tk.Tk()
MaFenetre.title("Jeu du casse-briques")
MaFenetre.geometry(centrer_fenetre(MaFenetre, 1000,600))
MaFenetre.config(bg="gray20")


# Frame du haut pour le score et les vies
FrameTop = tk.Frame(MaFenetre, bg="gray15", height=50)
FrameTop.pack(fill="x")

# Canvas pour le jeu
Zone_jeu = tk.Canvas(MaFenetre, bg="black", width=1000, height=500)
Zone_jeu.pack()

# Label pour le score 
Score=tk.StringVar()
LabelScore = tk.Label(FrameTop, textvariable=Score, fg="white", bg="gray15", font=("Arial", 14, "bold"))
LabelScore.pack(side="left", padx=20, pady=10)

# Label pour les vies
Vies=tk.StringVar()
LabelVies = tk.Label(FrameTop, textvariable=Vies, fg="white", bg="gray15", font=("Arial", 14, "bold"))
LabelVies.pack(side='right', padx=20, pady=10)

# Frame du bas pour les boutons
FrameBottom = tk.Frame(MaFenetre, bg="gray15", height=40)
FrameBottom.pack(side="bottom", fill="x")

# Boutons quitter et demarrer une nouvelle partie
Boutton_Quitter = tk.Button(FrameBottom, text="Quitter",command = MaFenetre.destroy)
Boutton_Quitter.pack(side="right", pady=10, padx=10)

# Bouton pour demarrer une nouvelle partie
Boutton_Demarrer = tk.Button(FrameBottom, text="Demarrer une nouvelle partie",command=demarrer)
Boutton_Demarrer.pack(side="left", pady=10, padx=10)

# Balle de test
balle1=b.balle(Zone_jeu,100,270,10,0,MaFenetre,"red",20)

# Plateforme   
plateforme = pl.plateforme(Zone_jeu,MaFenetre,600,450,50,20,"red")



MaFenetre.mainloop()

