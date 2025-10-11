#Jeronimo Gomez
#7/10/2025
#But: créer les classes pour le jeu de casses briques 

import math
import tkinter as tk
import Brique as br 





class balle:
    def __init__(self,canvas,x,y,rayon,vitesse,fenetre,couleur,angle):

        
        self.__fenetre=fenetre
        self.__canvas=canvas
        
        self.__x=x
        self.__y=y
        self.__rayon=rayon

        self.__angle=angle
        self.__vitesse=vitesse
        
        self.__dx=self.__vitesse*math.cos(self.__angle)
        self.__dy=self.__vitesse*math.sin(self.__angle)

        self.__couleur=couleur
        self.__boullee=self.__canvas.create_oval(self.__x-self.__rayon,self.__y-self.__rayon,self.__x+self.__rayon,self.__y+self.__rayon,fill=self.__couleur)

    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def getRayon(self):
        return self.__rayon
    
    def mouvement(self,brique_test):
        if  self.__x+self.__dx+self.__rayon > 1000:
            self.rebond_horizontal()
        if self.__x -self.__rayon +self.__dx <0:
            self.rebond_horizontal()
        if self.__y+self.__dy+self.__rayon > 520:
            self.detruire()
        if self.__y -self.__rayon +self.__dy <0:
            self.rebond_vertical()

        self.colision_balle_brique(brique_test)
        
        self.__x+=self.__dx
        self.__y+=self.__dy

        self.__canvas.coords(self.__boullee,self.__x-self.__rayon,self.__y-self.__rayon,self.__x+self.__rayon,self.__y+self.__rayon)
        self.__fenetre.after(20, self.mouvement, brique_test)

    def detruire(self):
        self.__canvas.delete(self.__boullee)
    
    def rebond_vertical(self):
        self.__dy=-self.__dy
    
    def rebond_horizontal(self):
        self.__dx=-self.__dx

    def colision_balle_brique(self, brique):
        x_balle = self.__x
        y_balle = self.__y

        x_brique = brique.getx()
        y_brique = brique.gety()
        largeur_brique = brique.getlargeur()
        hauteur_brique = brique.gethauteur()

        #colisition par le bas de la boulle et le haut de la brique
        if x_brique<= x_balle+self.__rayon <= x_brique + largeur_brique and y_brique <= y_balle+self.__rayon <= y_brique + 2:
            self.rebond_vertical()

        #colision par le haut de la boulle et le bas de la brique
        if x_brique<= x_balle+self.__rayon <= x_brique + largeur_brique and y_brique+hauteur_brique +8<= y_balle  <= y_brique+hauteur_brique + 10:
            self.rebond_vertical()



        
        
