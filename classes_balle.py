#Jeronimo Gomez
#7/10/2025
#But: créer les classes pour le jeu de casses briques 

import math
import tkinter as tk
import Brique as br 
import classe_plateforme as pl


class balle:
    # constructeur de la classe balle
    # Entrées: canvas,
    #          x,y: position initiale de la balle (entiers)
    #          rayon: rayon de la balle (entier)
    #          vitesse: vitesse initiale de la balle (entier)
    #          fenetre: fenetre principale (Tk)
    #          couleur: couleur de la balle (chaine de caracteres)
    #          angle: angle de depart de la balle (en radian)
    # Sorties: aucune
    def __init__(self,canvas,x,y,rayon,vitesse,fenetre,couleur,angle):

        
        self.__fenetre=fenetre
        self.__canvas=canvas
        
        self.__x=x
        self.__y=y
        self.__rayon=rayon

        self.__angle=angle
        self.__vitesse=vitesse
        
        self.__dx=self.__vitesse*math.cos(self.__angle) #composante horizontale de la vitesse
        self.__dy=self.__vitesse*math.sin(self.__angle) #composante verticale de la vitesse

        self.__couleur=couleur
        self.__boullee=self.__canvas.create_oval(self.__x-self.__rayon,self.__y-self.__rayon,self.__x+self.__rayon,self.__y+self.__rayon,fill=self.__couleur)

    # but: changer la vitesse de la balle, en changeant les composantes dx et dy
    # Entrées: nouvelle_vitesse (entier)
    # Sorties: aucune
    def changer_vitesse(self,nouvelle_vitesse):
        self.__dx = nouvelle_vitesse*math.cos(self.__angle)
        self.__dy = nouvelle_vitesse*math.sin(self.__angle)

    # but: detruire la balle du canvas
    # Entrées: aucune
    # Sorties: aucune        
    def detruire(self):
        self.__canvas.delete(self.__boullee)

    # but: faire rebondir la balle verticalement
    # Entrées: aucune
    # Sorties: aucune
    def rebond_vertical(self):
        self.__dy=-self.__dy

    # but: faire rebondir la balle horizontalement
    # Entrées: aucune
    # Sorties: aucune
    def rebond_horizontal(self):
        self.__dx=-self.__dx


    # but: detecter la colision entre la balle et une brique
    # Entrées: brique (objet de la classe Brique)
    # Sorties: aucune
    def colision_balle_brique(self, brique):
        
        if abs(self.__dx)<=5:
            x_balle = self.__x
            y_balle = self.__y
        else:
            x_balle = self.__x + self.__dx
            y_balle = self.__y + self.__dy
        
        marge = 3 # marge de colision,pour les cas limites 

        x_brique = brique.getx()
        y_brique = brique.gety()
        largeur_brique = brique.getlargeur()
        hauteur_brique = brique.gethauteur()

        # appliquer la fonction que si la brique n'as pas été détruite avant
        if brique.getvivant()==True:
    
            #colisition par le bas de la boulle et le haut de la brique
            if x_brique -marge <= x_balle <= x_brique + largeur_brique + marge and y_brique -marge <= y_balle+self.__rayon <= y_brique + marge:
                self.rebond_vertical()
                brique.detruire()
                

            #colision par le haut de la boulle et le bas de la brique
            if x_brique - marge<= x_balle <= x_brique + largeur_brique + marge and y_brique+ hauteur_brique -marge <= y_balle - self.__rayon <= y_brique+hauteur_brique + marge :
                self.rebond_vertical()
                brique.detruire()
                

            #colision par le cote gauche de la boulle et le cote droit de la brique
            if x_brique + largeur_brique - marge <= x_balle - self.__rayon <= x_brique + largeur_brique + marge and y_brique-marge <= y_balle <= y_brique + hauteur_brique+marge:
                self.rebond_horizontal()
                brique.detruire()
            
            #colision par le cote droite de la boulle et le cote gauche de la brique
            if x_brique - marge <= x_balle + self.__rayon <= x_brique + marge and y_brique -marge <= y_balle <= y_brique + hauteur_brique + marge:
                self.rebond_horizontal()
                brique.detruire()

        else:
            pass

    def collision_plateforme(self,plateforme):
          
        if abs(self.__dx)<=5:
            x_balle = self.__x
            y_balle = self.__y
        else:
            x_balle = self.__x + self.__dx
            y_balle = self.__y + self.__dy
        
        marge = 3 # marge de colision,pour les cas limites 

        x_plateforme = plateforme.getx()
        y_plateforme = plateforme.gety()
        largeur_plateforme = plateforme.getlargeur()
        

        if x_plateforme -marge <= x_balle <= x_plateforme + largeur_plateforme + marge and y_plateforme -marge <= y_balle+self.__rayon <= y_plateforme + marge:
                
                point_impact= (x_balle - x_plateforme + largeur_plateforme/2) / largeur_plateforme #entre 0 (gauche) et 1 (droite)

                self.rebond_vertical()
                #self.__angle = 60 + point_impact*(-10)
                #self.__dx = 

             

    
    

    
    
    def mouvement(self,liste_briques,plateforme):


        if  self.__x+self.__dx+self.__rayon > 1000:
            self.rebond_horizontal()
        if self.__x -self.__rayon +self.__dx <0:
            self.rebond_horizontal()
        if self.__y+self.__dy+self.__rayon > 520:
            self.detruire()
        if self.__y -self.__rayon +self.__dy <0:
            self.rebond_vertical()


        for i in range (len(liste_briques)):
            self.colision_balle_brique(liste_briques[i])
        
        self.collision_plateforme(plateforme)

        
        self.__x+=self.__dx
        self.__y+=self.__dy

        self.__canvas.coords(self.__boullee,self.__x-self.__rayon,self.__y-self.__rayon,self.__x+self.__rayon,self.__y+self.__rayon)
        self.__fenetre.after(20, self.mouvement, liste_briques,plateforme)

    



        
        
