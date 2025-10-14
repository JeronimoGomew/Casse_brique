#Jeronimo Gomez 
#7/10/2025
#but: créer la classe plateforme pour le jeu de casse briques
import tkinter as tk



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
        self.__canvas.bind('<Key>',self.bouger_plateforme)
        self.__canvas_width=self.__canvas.winfo_width()

    def bouger_plateforme(self,event):
        touche=event.keysym

        if touche == 'Right':
            self.__x += 20
        elif touche == 'Left':
            self.__x -= 20
        
        self.__canvas.coords(self.__plateforme, self.__x, self.__y, self.__x+ self.__largeur, self.__y + self.__hauteur, fill=self.__couleur)


        

        

 




