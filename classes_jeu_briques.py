#Jeronimo Gomez
#7/10/2025
#But: créer les classes pour le jeu de casses briques 

import math,random
import tkinter as tk


class balle:
    def __init__(self,canvas,x,y,rayon,vitesse,fenetre,couleur):

        
        self.__fenetre=fenetre
        self.__canvas=canvas
        
        self.__x=x
        self.__y=y
        self.__rayon=rayon

        self.__angle=random.uniform(0,2*math.pi)
        self.__vitesse=vitesse
        
        self.__dx=self.__vitesse*math.cos(self.__angle)
        self.__dy=self.__vitesse*math.sin(self.__angle)

        self.__couleur=couleur
        self.__boullee=self.__canvas.create_oval(self.__x-self.__rayon,self.__y-self.__rayon,self.__x+self.__rayon,self.__y+self.__rayon,fill=self.__couleur)
        self.__largeur=self.__canvas.winfo_width()
        self.__hauteur=self.__canvas.winfo_height()
    
    
    def mouvement(self):
        if  self.__x+self.__dx+self.__rayon > self.__largeur:
            self.__dx=-self.__dx
        if self.__x -self.__rayon +self.__dx <0:
            self.__dx=-self.__dx
        if self.__y+self.__dy+self.__rayon > self.__hauteur:
            self.__dy=-self.__dy
        if self.__y -self.__rayon +self.__dy <0:
            self.__dy=-self.__dy
        
        self.__x+=self.__dx
        self.__y+=self.__dy

        self.__canvas.coords(self.__boullee,self.__x-self.__rayon,self.__y-self.__rayon,self.__x+self.__rayon,self.__y+self.__rayon)
        self.__fenetre.after(20,self.mouvement)



class plateforme:
    def __init__(self,canvas,fenetre,x,y,largeur,hauteur,couleur):
        self.__canvas=canvas
        self.__fenetre=fenetre
        self.__x=x
        self.__y=y
        self.__largeur=largeur
        self.__hauteur=hauteur
        self.__couleur=couleur

        self.__plateforme=self.__canvas.create_rectangle(self.__x,self.__y,self.__x+self.__largeur,self.__y+self.__hauteur,fill=self.__couleur)
        self.__canvas.bind_all("<KeyPress-Left>",self.gauche)
        self.__canvas.bind_all("<KeyPress-Right>",self.droite)
        self.__canvas_width=self.__canvas.winfo_width()