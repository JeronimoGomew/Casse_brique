"""
Daoud Hechaichi et Jeronimo Gomez
7/10/2025
but: créer la classe brique
a améliorer: faire que les bonus s'obtiennent que lorsque la platforme touche les gifs qui descendent
"""

from tkinter import N
from PIL import Image,ImageTk
from Classe_bonus import Bonus


class Brique:
    """
    constructeur de la classe Brique, des rectangles qui se cassent au contact avec la balle.
    il y a aussi des sousclasses avec des briques spéciaux
 
    Entrées: Canvas, canvas ou seron les briques (Canvas)
             x,y: coordonnées du coin superieur gauche des briques (entier)
             largeur: largeur des briques (entier)
             hauteur: hauteur des briques (entier)
             couleur: couleur des briques (str)
"""
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
    
   
    def enlever_vie (self):
        """
        #but: detruire le brique
        #Entrées: Rien
        #Sorties: Rien
        """
        self._vie -=1

        if self._vie==0:
            self.detruire()
        else:
            return
    

    def detruire (self):
         self._canvas.delete(self._brique)


    def changer_couleur(self,couleur):
        self._canvas.itemconfigure(self._brique,fill=couleur)

        
class Brique_2vies(Brique):
    def __init__(self, canvas, x, y, largeur, hauteur):
        """
     héritage de la classe Brique
     Brique avec deux vies, (se casse avec duex contacts avec la balle)
     """
        super().__init__(canvas, x, y, largeur, hauteur)#a utiliser car les variables de Brique sont privées
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
    


class Brique_indestructible(Brique):
    """
    héritage de la classe Brique
    brique qui ne se détruit pas
        """
    def __init__(self, canvas, x, y, largeur, hauteur):
        super().__init__(canvas, x, y, largeur, hauteur)
        self._couleur="grey"
        self.changer_couleur(self._couleur)
    
    
    def enlever_vie(self):
        return #on ne peut pas enlever la vie de la brique, cette fonction ne fait rien


class Brique_rapide(Brique):
    def __init__(self,canvas,x,y,largeur,hauteur,fenetre,plateforme,Bonus):

        super().__init__(canvas, x, y, largeur, hauteur)
        self._fenetre = fenetre
        self._plateforme = plateforme
        self._Bonus = Bonus

        self._gif=Image.open("LAPIN.gif")
        self._gif_bonnetaille=self._gif.resize((70,70))#change la taille du gif pour l'adater
        self._gif_definitif=ImageTk.PhotoImage(self._gif_bonnetaille)#initialise l'image pour tkinter


        self._Ximage= (self._x + self._largeur/2)#coordonnées de l'image
        self._Yimage= (self._y-30) #-30 aojuté a l'oeil pour que l'image rentre dans la brique
        self.changer_couleur("orange")

        self._dif_vitesse=30 #vitesse qui sera ajoutée a la vitesse initiale
        self._gif_canvas=self._canvas.create_image(self._Ximage,self._Yimage,image= self._gif_definitif, anchor=N)
        #creation de l'image dans le canvas


    def bouger_gif(self):
        """"
        Entree: rien
        Sorite: rien
        but: faire descendre le gif et le detruire lorsqu'il dépasse les limites du canvas
        """
        dy=3
        self._Yimage += dy
        self._canvas.coords(self._gif_canvas,self._Ximage,self._Yimage)
        
        
        if self._Yimage>400:
            self._canvas.delete(self._gif_canvas)
            return
        
        self._fenetre.after(10,self.bouger_gif)


    def detruire(self):
        """"
        entrées: rien
        sorties: rien

        but: detruire le brique, le gif statique, créer un gif pour le faire descendre
        puis executer le bonus géré par la classe bonus
        """
        
        self._canvas.delete(self._gif_canvas)
        self._canvas.delete(self._brique)

        self._gif_canvas=self._canvas.create_image(self._Ximage,self._Yimage,image= self._gif_definitif, anchor=N)
        self.bouger_gif()
        self.bonus()

    
    def bonus(self):
        """"
        entrée: rien
        sortie: rien
        but: gérer les bonus
        """
        self._Bonus.ajouter_bonus(self._dif_vitesse)



class Brique_lent(Brique_rapide):
    def __init__(self,canvas,x,y,largeur,hauteur,fenetre,plateforme,Bonus):

        super().__init__(canvas, x, y, largeur, hauteur,fenetre,plateforme,Bonus)
        
        #nouvelle image
        self._gif=Image.open("TORTUE.gif")
        self._gif_bonnetaille=self._gif.resize((60,60))
        self._gif_definitif=ImageTk.PhotoImage(self._gif_bonnetaille)
        self._Yimage=(self._y-10)
        self._gif_canvas=self._canvas.create_image(self._Ximage,self._Yimage,image= self._gif_definitif, anchor=N)
                                                   
        self._dif_vitesse=(-15)#on ajoute une valeur négative a la vitesse initialle

    
        self.changer_couleur("yellow")



        
   


    

        
    
    







       




