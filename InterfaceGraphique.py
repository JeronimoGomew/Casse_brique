import tkinter as tk
import classes_balle as b
import Brique as br

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
    global vitesse
    vitesse=5
    balle1=b.balle(Zone_jeu,10,400,10,vitesse,MaFenetre,"red",10)
    brique_test = br.Brique(Zone_jeu, 800, 200, 120, 40, "blue")
    balle1.mouvement(brique_test)
    #balleinit.detruire()


# Programme principal
# Initialisation de la fenetre principale, titre, dimensions et couleur de fond 
MaFenetre = tk.Tk()
MaFenetre.title("Jeu du casse-briques")
MaFenetre.geometry(centrer_fenetre(MaFenetre, 1000, 600))
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

#Balle de test
balleinit=b.balle(Zone_jeu,800,190,10,0,MaFenetre,"blue",10)






MaFenetre.mainloop()

