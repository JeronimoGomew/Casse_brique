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
        self.__vie = 1 #variable utile dans le programme pour éviter les colisions avec le brique lorsqu'il
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
    def getvie(self):
        return self.__vie
    
    #but: detruire le brique
    #Entrées: Rien
    #Sorties: Rien
    def enlever_vie (self):
        self.__vie -=1

        if self.__vie==0:
            self.__canvas.delete(self.__brique)
        else:
            return
        

#héritage de la classe Brique
#Brique avec deux vies
class Brique_2vies(Brique):
    def enlever_vie(self):
        self.__vie -=0.5

        if self.__vie==0:
            self.__canvas.delete(self.__brique)
        else:
            return


#héritage de la classe Brique
#brique qui ne se détruit pas
class Brique_indestructible(Brique):
    def enlever_vie(self):
        return





       




