import tkinter as tk
import random as rd
import math as mt



MaFenetre = tk.Tk()
MaFenetre.title ("Jeu du casse-briques")
MaFenetre.geometry("1000x600")
MaFenetre.config(bg="gray20")
Canvas = tk.Canvas(MaFenetre, bg="black")
Canvas.pack(fill="both", expand=True)

class Brique:
    def __init__(self , canvas, x, y, largeur, hauteur, couleur):
        self._canvas = canvas
        self._x = x
        self._y = y
        self._largeur = largeur
        self._hauteur = hauteur
        
        self._brique = self._canvas.create_rectangle(x, y, x + largeur, y + hauteur, fill=couleur)
        self._couleur = couleur     

brique_test = Brique(Canvas, 100, 100, 120, 40, "red")

if __name__ == "__main__":
    MaFenetre.mainloop()

