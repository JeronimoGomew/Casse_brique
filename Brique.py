#Daoud Hechaichi et Jeronimo Gomez
#7/10/2025
#but: créer la classe brique
#a améliorer: créer des briques spéciaux

class Brique:
    #constructeur de la classe Brique
    #Entrées: Canvas, canvas ou seron les briques (Canvas)
    #         x,y: coordonnées du coin superieur gauche des briques (entier)
    #         largeur: largeur des briques (entier)
    #         hauteur: hauteur des briques (entier)
    #         couleur: couleur des briques (str)

    def __init__(self , canvas, x, y, largeur, hauteur, couleur):
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        self.__largeur = largeur
        self.__hauteur = hauteur
        self.__couleur = couleur 
        self.__vivant = True #variable utile dans le programme pour éviter les colisions avec le brique lorsqu'il
                             #est détruit
        
        # création du brique dans le Canvas
        self.__brique = self.__canvas.create_rectangle(x, y, x + largeur, y + hauteur, fill=couleur)


    #getteurs de coordonées, largeur,hauteur, et vivant
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def getlargeur(self):
        return self.__largeur    
    def gethauteur(self):
        return self.__hauteur
    def getvivant(self):
        return self.__vivant
    
    #but: detruire le brique
    #Entrées: Rien
    #Sorties: Rien
    def detruire (self):
        self.__canvas.delete(self.__brique)
        self.__vivant = False

       




