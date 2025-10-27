"""
Jeronimo Gomez et Daoud Hechaichi
7/10/2025
But: créer la classe balle pour le jeu de casses briques 
"""
from math import cos,sin,sqrt,radians
from Brique import Brique, Brique_indestructible,Brique_2vies,Brique_lent,Brique_rapide
from random import randint

""""
Sommaire de fonctions:
 initialisation
 changer_vitesse
 detruire
 getteur de difficulté
 rebond vertical
 rebond horizontal
 liste de briques
 collision_balle_brique
 collision_plateforme
 suivre_plateforme
 mettre a jour les coordonées depuis le Canvas
 mouvement
"""

class balle:
    """
     constructeur de la classe balle
     Entrées: canvas: canvas ou la balle sera dessinée
              x,y: coords initiales de la balle, on fait en sorte qu'elles soient au milieu de la boulle (entiers)
              rayon: rayon de la balle (entier)
              vitesse: vitesse initiale de la balle (entier)
              fenetre: fenetre principale (Tk)
              couleur: couleur de la balle (chaine de caracteres)
              angle: angle de depart de la balle (en radian)
     Sorties: aucune
    """
    def __init__(self,canvas,x,y,rayon,vitesse,fenetre,couleur,angle,liste_briques,difficulte,plateforme,Bonus):

        self.__liste_briques=liste_briques
        self.__fenetre=fenetre
        self.__canvas=canvas
        self.__difficulte=difficulte
        self.__plateforme=plateforme
        self.__Bonus=Bonus
        
        self.__x=x
        self.__y=y
        self.__rayon=rayon

        self.__angle = radians(angle)
        self.__vitesse=vitesse #vitesse initiale
        
        self.__dx=self.__vitesse*cos(self.__angle) #composante horizontale de la vitesse
        self.__dy=self.__vitesse*sin(self.__angle) #composante verticale de la vitesse

        self.__couleur=couleur
        self.__boullee=self.__canvas.create_oval(self.__x-self.__rayon,self.__y-self.__rayon,self.__x+self.__rayon,self.__y+self.__rayon,fill=self.__couleur)




    def changer_vitesse(self, nouvelle_vitesse):
        self.__vitesse = nouvelle_vitesse
        self.__dx = self.__vitesse * cos(self.__angle)
        self.__dy = self.__vitesse * sin(self.__angle)

    #getteurs
    def get_difficulte(self):
        return(self.__difficulte)  
    def get_vitesse(self):
        return(self.__vitesse)

        
    def detruire(self):
        """
        but: detruire la balle du canvas
        Entrées: aucune
        Sorties: aucune 
        """
      
        self.__canvas.delete(self.__boullee)


    def rebond_vertical(self):
        '''
            # but: faire rebondir la balle verticalement
    # Entrées: aucune
    # Sorties: aucune
    '''
        self.__dy=-self.__dy

    
    def rebond_horizontal(self):
        """
    # but: faire rebondir la balle horizontalement
    # Entrées: aucune
    # Sorties: aucune
    """
        self.__dx=-self.__dx


    def liste_briques(self):
        """""
        but: créer une liste de briques adaptés à la fenetre du jeu, en ajoutan de facon aléatoire des briques
        spéciaux
        entrées: rien
        sortie: liste de briques à insérer dans la classe balle
        """
        num_colonnes = 8
        dico_briques = {0: list(range(num_colonnes)),1: list(range(num_colonnes)),2: list(range(num_colonnes)),3:list(range(num_colonnes))}
        liste_br = []
        briques_speciaux=[]

        for l in range(5+self.__difficulte):
            #au début on choisit de mettre cinq briques spéciaux
            #avec cette boucle on a leurs coordonnées de facon aléatoire, et sans répeter entre elles
            ligne_aleatoire = randint(0,3) 
            colonne_aleatoire = randint(0,(len(dico_briques[ligne_aleatoire])-1))
            

            #coordonées (ligne,colonne) stockées dans la liste briques spéciaux
            briques_speciaux.append([ligne_aleatoire,dico_briques[ligne_aleatoire][colonne_aleatoire]])
            
            #on pop, pour ne pas répeter la colonne 
            dico_briques[ligne_aleatoire].pop(colonne_aleatoire)
        
        

        # on crée 4 lignes et 8 colonnes de briques 
        for j in range (4):
            for i in range (num_colonnes):
                    largeur = 90
                    hauteur = 40
                    x = 9 + largeur + i*(9+largeur)
                    y = 10 + 50*j
                    
                    brique=Brique(self.__canvas,x,y,largeur,hauteur)
                    liste_br.append(brique)

        
        
        for l,coords in enumerate(briques_speciaux):
            
            #on choisit un brique parmi les 4 briques spéciaux
            quel_brique = l%4

            largeur=90
            hauteur=40
            x = 9 + largeur + (coords[1])*(9+largeur)
            y = 10 + 50*coords[0]

            #comme la liste_briques a une seule dimension, alors on transforme les coordonées de la liste de 
            #briques spéciaux (qui a 2 dimensions) en un index de une dimension qui correspond.   
            index_liste = coords[0]*num_colonnes + (coords[1])
            #on detruit le brique normal qui était a cétte cordonné
            liste_br[index_liste].detruire()

            #on le remplace par le brique spécial
            if quel_brique==0:
                liste_br[index_liste]=Brique_2vies(self.__canvas,x,y,largeur,hauteur)

            elif quel_brique==1:
                liste_br[index_liste]=Brique_indestructible(self.__canvas,x,y,largeur,hauteur)
            
            elif quel_brique==2:
                liste_br[index_liste]=Brique_rapide(self.__canvas,x,y,largeur,hauteur,self.__fenetre,self.__plateforme,self.__Bonus)

            elif quel_brique==3:
                liste_br[index_liste]=Brique_lent(self.__canvas,x,y,largeur,hauteur,self.__fenetre,self.__plateforme,self.__Bonus)
         
        return liste_br

  
    def colision_balle_brique(self, brique,score):
        """
        but: detecter la colision entre la balle et une brique, en detruisant la brique et ajoutant un point
        Entrées: brique (objet de la classe Brique)
                 score (objet de la classe score)
        Sorties: aucune
        
        """

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
        if brique.getvie()>0:
    
            #colisition par le bas de la boulle et le haut de la brique
            if x_brique -marge <= x_balle <= x_brique + largeur_brique + marge and y_brique -marge <= y_balle+self.__rayon <= y_brique + marge:
                self.rebond_vertical()
                brique.enlever_vie()
                if type(brique) is Brique_indestructible:
                    return 0
                else:
                    score.ajouter_point()
                return 0

                

            #colision par le haut de la boulle et le bas de la brique
            if x_brique - marge<= x_balle <= x_brique + largeur_brique + marge and y_brique+ hauteur_brique -marge <= y_balle - self.__rayon <= y_brique+hauteur_brique + marge :
                self.rebond_vertical()
                brique.enlever_vie()
                if type(brique) is Brique_indestructible:
                    return 0
                else:
                    score.ajouter_point()
                return 0
                

            #colision par le cote gauche de la boulle et le cote droit de la brique
            if x_brique + largeur_brique - marge <= x_balle - self.__rayon <= x_brique + largeur_brique + marge and y_brique-marge <= y_balle <= y_brique + hauteur_brique+marge:
                self.rebond_horizontal()
                brique.enlever_vie()
                if type(brique) is Brique_indestructible:
                    return 0
                else:
                    score.ajouter_point()
                return 0
            
            #colision par le cote droite de la boulle et le cote gauche de la brique
            if x_brique - marge <= x_balle + self.__rayon <= x_brique + marge and y_brique -marge <= y_balle <= y_brique + hauteur_brique + marge:
                self.rebond_horizontal()
                brique.enlever_vie()
                if type(brique) is Brique_indestructible:
                    return 0
                else:
                    score.ajouter_point()
                return 0

        else:
            pass

   
    def collision_plateforme(self,plateforme):
        """
        but: gérer la colision avec la plateforme, en utilisant le principe de Descartes
        Entrée: plateforme (classe plateforme)
        Sortie : Rien
          """
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
    
   
    def suivre_plateforme(self,plateforme):
        """
         but: fonction qui fait que la balle reste sur la plateforme au début du jeu
        Entrée: plateforme
        sortie: Rien
            """
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
            self.__fenetre.after(10,self.suivre_plateforme,plateforme)
            return True
        else:
            return 
            
    
    def mettre_a_jour_position_depuis_canvas(self):
        """"
        but: mettre a jour les coordonés de la balle dans le programme principal pour initialiser le jeu
        entrée: rien
        sortie : rien 
        """
        coords = self.__canvas.coords(self.__boullee)  # (x1, y1, x2, y2)
        self.__x = (coords[0] + coords[2]) / 2 # donne la coordonée x du centre de la boulle
        self.__y = (coords[1] + coords[3]) / 2 # donne la coordonnée y du centre de la boulle

     
    def mouvement(self,plateforme,vies,score):
        """""
        but: gérer le mouvement de la balle, le score et les vies 
        #entrées: plateforme (classe plateforme)
                  vies       (classe vies)
                  score       (classe score)
        sorties:rien
        """""

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
        
        #enlever le brique de la liste s'il est détruit ou s'il est indesctrubtible, comme ca, si on relance il ne réapparait pas
        for brique in self.__liste_briques:
            brique_indestructible = 0
            if brique.getvie()==0:
                self.__liste_briques.remove(brique)
            if type(brique) is Brique_indestructible:
                brique_indestructible += 1
        
        #s'il n'y a plus de briques, arreter la balle et reinitialiser les briques en augmentant la vitesse
        if self.__liste_briques==[] or len(self.__liste_briques) == brique_indestructible :
            self.changer_vitesse(0)
            self.suivre_plateforme(plateforme)
            self.__difficulte += 1
            
            for brique in self.__liste_briques:
                brique.detruire()#pour les briques indestructibles
            self.__liste_briques = self.liste_briques()#créer des nouveaux briques
            score.ajouter_niveau()#ajouter un diamond
            return 
        
         
                    


        
        #gérer la collision avec la plateforme
        self.collision_plateforme(plateforme)

        #change les coordonées
        self.__x+=self.__dx
        self.__y+=self.__dy

        #met a jour la fenetre avec les nouvelles coordonnées et relance la fonction mouvement chaque 10 ms
        self.__canvas.coords(self.__boullee,self.__x-self.__rayon,self.__y-self.__rayon,self.__x+self.__rayon,self.__y+self.__rayon)
        self.__fenetre.after(10, self.mouvement,plateforme,vies,score)

    



        
        
