#Jeronimo Gomez
#7/10/2025
#But: créer la classe balle pour le jeu de casses briques 

from math import cos,sin,sqrt,radians
from Brique import Brique

#Sommaire de fonctions:
# initialisation
# changer_vitesse
# detruire
# getteur de difficulté
# rebond vertical
# rebond horizontal
# liste de briques
# collision_balle_brique
# collision_plateforme
# suivre_plateforme
# mettre a jour les coordonées depuis le Canvas
# mouvement




class balle:
    # constructeur de la classe balle
    # Entrées: canvas: canvas ou la balle sera dessinée
    #          x,y: coords initiales de la balle, on fait en sorte qu'elles soient au milieu de la boulle (entiers)
    #          rayon: rayon de la balle (entier)
    #          vitesse: vitesse initiale de la balle (entier)
    #          fenetre: fenetre principale (Tk)
    #          couleur: couleur de la balle (chaine de caracteres)
    #          angle: angle de depart de la balle (en radian)
    # Sorties: aucune
    def __init__(self,canvas,x,y,rayon,vitesse,fenetre,couleur,angle,liste_briques,difficulte):

        self.__liste_briques=liste_briques
        self.__fenetre=fenetre
        self.__canvas=canvas
        self.__difficulte=difficulte
        
        self.__x=x
        self.__y=y
        self.__rayon=rayon

        self.__angle=angle
        self.__vitesse=vitesse #vitesse initiale
        
        self.__dx=self.__vitesse*cos(self.__angle) #composante horizontale de la vitesse
        self.__dy=self.__vitesse*sin(self.__angle) #composante verticale de la vitesse

        self.__couleur=couleur
        self.__boullee=self.__canvas.create_oval(self.__x-self.__rayon,self.__y-self.__rayon,self.__x+self.__rayon,self.__y+self.__rayon,fill=self.__couleur)

    # but: changer la vitesse de la balle, en changeant les composantes dx et dy
    # Entrées: nouvelle_vitesse (entier)
    # Sorties: aucune
    def changer_vitesse(self,nouvelle_vitesse):
        self.__dx = nouvelle_vitesse*cos(self.__angle)
        self.__dy = nouvelle_vitesse*sin(self.__angle)

    #getteur de difficulté
    def get_difficulte(self):
        return(self.__difficulte)

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

    def liste_briques(self):

        liste_br = []

        #on crée 4 lignes et 10 colonnes de briques 
        for j in range (4):
            for i in range (10):
                brique=Brique(self.__canvas,9 + i*90 + i*9,10 + 50*j,90,40,"blue")
                liste_br.append(brique)
        return liste_br


    # but: detecter la colision entre la balle et une brique, en detruisant la brique et ajoutant un point
    # Entrées: brique (objet de la classe Brique)
    # Sorties: aucune
    def colision_balle_brique(self, brique,score):
        
        #prédire la position si la balle va vite
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
        if brique.getvie()==1:
    
            #colisition par le bas de la boulle et le haut de la brique
            if x_brique -marge <= x_balle <= x_brique + largeur_brique + marge and y_brique -marge <= y_balle+self.__rayon <= y_brique + marge:
                self.rebond_vertical()
                brique.enlever_vie()
                score.ajouter_point()
                return 0

                

            #colision par le haut de la boulle et le bas de la brique
            if x_brique - marge<= x_balle <= x_brique + largeur_brique + marge and y_brique+ hauteur_brique -marge <= y_balle - self.__rayon <= y_brique+hauteur_brique + marge :
                self.rebond_vertical()
                brique.enlever_vie()
                score.ajouter_point()
                return 0
                

            #colision par le cote gauche de la boulle et le cote droit de la brique
            if x_brique + largeur_brique - marge <= x_balle - self.__rayon <= x_brique + largeur_brique + marge and y_brique-marge <= y_balle <= y_brique + hauteur_brique+marge:
                self.rebond_horizontal()
                brique.enlever_vie()
                score.ajouter_point()
                return 0
            
            #colision par le cote droite de la boulle et le cote gauche de la brique
            if x_brique - marge <= x_balle + self.__rayon <= x_brique + marge and y_brique -marge <= y_balle <= y_brique + hauteur_brique + marge:
                self.rebond_horizontal()
                brique.enlever_vie()
                score.ajouter_point()
                return 0

        else:
            pass

    #but: gérer la colision avec la plateforme, en utilisant le principe de Descartes
    #Entrée: plateforme (rectangle dans un Canvas)
    #Sortie : Rien
    def collision_plateforme(self,plateforme):
          
         #prediction de la position si la balle va vite  
        if abs(self.__dx)<=5:
            x_balle = self.__x
            y_balle = self.__y
        else:
            x_balle = self.__x + self.__dx
            y_balle = self.__y + self.__dy
        
        marge = 3 # marge de colision,pour les cas limites 

        #coordonées et largeur de la plateforme.
        x_plateforme = plateforme.getx()
        y_plateforme = plateforme.gety()
        largeur_plateforme = plateforme.getlargeur()
        
        #detecte la collision de la balle avec la plateforme
        if x_plateforme -marge <= x_balle <= x_plateforme + largeur_plateforme + marge and y_plateforme -marge <= y_balle+self.__rayon <= y_plateforme + marge:
                
                
             #Calcul du point d’impact
            position_relative = (x_balle - x_plateforme) / largeur_plateforme  # entre 0 (gauche) et 1 (droite)
            position_centrée = (position_relative - 0.5) * 2  # entre -1 (gauche) et +1 (droite)

            #angle limite (la balle rebondit avec cette angle si elle tape le coin de la plateforme)
            angle_max = radians(60)
            nouvel_angle = position_centrée * angle_max

                 

            # Mise à jour des composantes de vitesse
            vitesse = sqrt(self.__dx**2 + self.__dy**2)
            self.__dx = vitesse * sin(nouvel_angle)   # rebond horizontal
            self.__dy = -vitesse * cos(nouvel_angle)  # rebond vertical

            # Ajuste légèrement la position pour éviter que la balle rébondisse vers le bas immédiatement
            self.__y = y_plateforme - self.__rayon - 1
    

    #but: fonction qui fait que la balle reste sur la plateforme au début du jeu
    #Entrée: plateforme
    #sortie: Rien
    def suivre_plateforme(self,plateforme):
        x_plat = plateforme.getx()
        y_plat = plateforme.gety()
        largeur_plat = plateforme.getlargeur()
        
        #coordonées X et Y pour que la balle soit au milieu de la platforme
        X=x_plat + largeur_plat/2 -self.__rayon
        Y=y_plat - 2*self.__rayon 

        #la fonction s'applique que si la vitesse de la balle est nulle, ca nous servira pour démarrer
        #le jeu et dans la fonction mouvement
        if self.__dx==0 and self.__dy==0:
            self.__canvas.coords(self.__boullee,X,Y,X+2*self.__rayon,Y+2*self.__rayon)
            self.__fenetre.after(20,self.suivre_plateforme,plateforme)
        else:
            return
            
    #but: mettre a jour les coordonés de la balle dans le programme principal pour initialiser le jeu
    #entrée: rien
    #sortie : rien 
    def mettre_a_jour_position_depuis_canvas(self):
        coords = self.__canvas.coords(self.__boullee)  # (x1, y1, x2, y2)
        self.__x = (coords[0] + coords[2]) / 2 # donne la coordonée x du centre de la boulle
        self.__y = (coords[1] + coords[3]) / 2 # donne la coordonnée y du centre de la boulle

    #but: gérer le mouvement de la balle 
    #entrées: 
    def mouvement(self,plateforme,vies,score):

        #rebond avec la paroi droite du canvas
        if  self.__x+self.__dx+self.__rayon > 1000:
            self.rebond_horizontal()
        
        #rebond avec la paroi gauche du canvas
        if self.__x -self.__rayon +self.__dx <0:
            self.rebond_horizontal()
        
        #si la balle depase le limite d'en bas du canvas, reinitialiser la balle et enlever une vie
        if self.__y+self.__dy+self.__rayon > 520:
          
            if vies.getnbvies()>1:
                self.changer_vitesse(0)
                self.suivre_plateforme(plateforme)
                vies.perdre_vie()
                return
            
            #si l'utilisateur n'as plus de vies
            else:
                vies.perdre_vie()
                self.detruire()
                self.__canvas.create_text(500,250,text="GAME OVER",fill='red',font=("Comic Sans MS",32))
                self.__canvas.update()
                return 

        #rebond avec la paroi d'en haut du canvas
        if self.__y -self.__rayon +self.__dy <0:
            self.rebond_vertical()

        #gérer la colision avec tous les briques 
        for i in range (len(self.__liste_briques)):
            self.colision_balle_brique(self.__liste_briques[i],score)
        
        #enlever le brique de la liste s'il est détruit, comme ca, si on relance il ne réapparait pas
        for brique in self.__liste_briques:
            if brique.getvie()==0:
                self.__liste_briques.remove(brique)
        
        #s'il n'y a plus de briques, arreter la balle et reinitialiser les briques en augmentant la vitesse
        if self.__liste_briques==[]:
            self.changer_vitesse(0)
            self.suivre_plateforme(plateforme)
            self.__difficulte += 1
            self.__liste_briques = self.liste_briques()
            self.__angle = radians(90)                      #reinitialise l'angle de départ
            self.__dx = self.__vitesse * sin(self.__angle)  #reinitialise le vecteur vitesse avec les nouveaux valeurs
            self.__dy = self.__vitesse * cos(self.__angle) 
            return 
                    


        
        #gérer la collision avec la plateforme
        self.collision_plateforme(plateforme)

        #change les coordonées
        self.__x+=self.__dx
        self.__y+=self.__dy

        #met a jour le canvas avec les nouvelles coordonnées et relance la fonction mouvement chaque 10 ms
        self.__canvas.coords(self.__boullee,self.__x-self.__rayon,self.__y-self.__rayon,self.__x+self.__rayon,self.__y+self.__rayon)
        self.__fenetre.after(10, self.mouvement,plateforme,vies,score)

    



        
        
