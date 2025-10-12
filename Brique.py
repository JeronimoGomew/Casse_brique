import tkinter as tk
import random as rd
import math as mt


class Brique:
    def __init__(self , canvas, x, y, largeur, hauteur, couleur):
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        self.__largeur = largeur
        self.__hauteur = hauteur
        self.__couleur = couleur 
        self.__vivant = True 
        
        self.__brique = self.__canvas.create_rectangle(x, y, x + largeur, y + hauteur, fill=couleur)

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
    
    def detruire (self):
        self.__canvas.delete(self.__brique)
        self.__vivant = False
 
        




