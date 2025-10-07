#Jeronimo Gomez
#7/10/2025
#But: créer les classes pour le jeu de casses briques 

class boule:
    def __init__(self, x, y, rayon, couleur, vitesse_x, vitesse_y):
        self.x = x
        self.y = y
        self.rayon = rayon
        self.couleur = couleur
        self.vitesse_x = vitesse_x
        self.vitesse_y = vitesse_y
    
    def deplacer(self):
        self.x += self.vitesse_x
        self.y += self.vitesse_y
    
    def rebondir(self, largeur_fenetre, hauteur_fenetre):
        if 