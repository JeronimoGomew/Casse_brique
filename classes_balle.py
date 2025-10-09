#Jeronimo Gomez
#7/10/2025
#But: créer les classes pour le jeu de casses briques 

import math,random
import tkinter as tk


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
    
    def mouvement(self):
        if  self.__x+self.__dx+self.__rayon > 1000:
            self.__dx=-self.__dx
        if self.__x -self.__rayon +self.__dx <0:
            self.__dx=-self.__dx
        if self.__y+self.__dy+self.__rayon > 500:
            self.__dy=-self.__dy
        if self.__y -self.__rayon +self.__dy <0:
            self.__dy=-self.__dy
        
        self.__x+=self.__dx
        self.__y+=self.__dy

        self.__canvas.coords(self.__boullee,self.__x-self.__rayon,self.__y-self.__rayon,self.__x+self.__rayon,self.__y+self.__rayon)
        self.__fenetre.after(20,self.mouvement)



