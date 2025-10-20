#Daoud Hechaichi et Jeronimo Gomez
#7/10/2025
#but: créer la classe brique
#a améliorer: créer des briques spéciaux

class Brique:
    #constructeur de la classe Brique, des rectangles qui se cassent au contact avec la balle.
    #il y a aussi des sousclasses avec des briques spéciaux
 
    #Entrées: Canvas, canvas ou seron les briques (Canvas)
    #         x,y: coordonnées du coin superieur gauche des briques (entier)
    #         largeur: largeur des briques (entier)
    #         hauteur: hauteur des briques (entier)
    #         couleur: couleur des briques (str)

    def __init__(self , canvas, x, y, largeur, hauteur):
        self._canvas = canvas
        self._x = x
        self._y = y
        self._largeur = largeur
        self._hauteur = hauteur
        self._couleur = "blue" 
        self._vie = 1 #variable utile dans le programme pour éviter les colisions avec le brique lorsqu'il
                             #est détruit
        
        # création du brique dans le Canvas
        self._brique = self._canvas.create_rectangle(x, y, x + largeur, y + hauteur, fill=self._couleur)


    #getteurs de coordonées, largeur,hauteur, et vivant
    def getx(self):
        return self._x
    def gety(self):
        return self._y
    def getlargeur(self):
        return self._largeur    
    def gethauteur(self):
        return self._hauteur
    def getvie(self):
        return self._vie
    
    #but: detruire le brique
    #Entrées: Rien
    #Sorties: Rien
    def enlever_vie (self):
        self._vie -=1

        if self._vie==0:
            self.detruire()
        else:
            return
    
    def detruire (self):
         self._canvas.delete(self._brique)
        
    def changer_couleur(self,couleur):
        self._canvas.itemconfigure(self._brique,fill=couleur)

        

#héritage de la classe Brique
#Brique avec deux vies, (se casse avec duex contacts avec la balle)
class Brique_2vies(Brique):
    def __init__(self, canvas, x, y, largeur, hauteur):
        super().__init__(canvas, x, y, largeur, hauteur)
        self._vie = 2
        self._couleur="green"
        self.changer_couleur(self._couleur)
    
    def enlever_vie (self):
        self._vie -=1
        self.changer_couleur("blue")

        if self._vie==0:
            self.detruire()
        else:
            return
    


#héritage de la classe Brique
#brique qui ne se détruit pas
class Brique_indestructible(Brique):
    def __init__(self, canvas, x, y, largeur, hauteur):
        super().__init__(canvas, x, y, largeur, hauteur)
        self._couleur="grey"
        self.changer_couleur(self._couleur)
    
    
    def enlever_vie(self):
        return





       




