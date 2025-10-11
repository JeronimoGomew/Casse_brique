import tkinter as tk
import random as rd
import math as mt


class Brique:
    def __init__(self , canvas, x, y, largeur, hauteur, couleur):
        self._canvas = canvas
        self._x = x
        self._y = y
        self._largeur = largeur
        self._hauteur = hauteur
        self._couleur = couleur 
        
        self._brique = self._canvas.create_rectangle(x, y, x + largeur, y + hauteur, fill=couleur)

    def getx(self):
        return self._x
    def gety(self):
        return self._y
    def getlargeur(self):
        return self._largeur    
    def gethauteur(self):
        return self._hauteur
        




