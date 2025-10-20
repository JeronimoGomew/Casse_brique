#Jeronimo Gomez 
#7/10/2025
#but: créer la classe plateforme pour le jeu de casse briques

class plateforme:
    #constructeur de la classe plateforme, un rectangle que l'utilisateur controle avec les fleches du clavier 
    #Entrées: canvas,canvas ou la balle sera dessinée (Canvas)
    #         x,y: coordonées du coin superieur gauche de la plateforme (entiers)
    #         larguer: larguer de la plateforme (entier)
    #         hauteur: hauteur de la plateforme (entier)
    #         couleur: couleur de la plateforme (str)
            
    def __init__(self,canvas,x,y,largeur,hauteur,couleur):
        self.__canvas=canvas
        self.__x=x
        self.__y=y
        self.__largeur=largeur
        self.__hauteur=hauteur
        self.__couleur=couleur

        # création du rectangle dans le canvas
        self.__plateforme=self.__canvas.create_rectangle(self.__x,self.__y,self.__x+self.__largeur,self.__y+self.__hauteur,fill=self.__couleur)
        
        # focus sur le canvas et récuperation que des fleches droite et gauche du clavier
        self.__canvas.focus_set()
        self.__canvas.bind('<Left>',self.bouger_plateforme)
        self.__canvas.bind('<Right>',self.bouger_plateforme)
        
       
    #getteurs des coordonnées, largeur et hauteur de la plateforme
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def getlargeur(self):
        return self.__largeur
    def gethauteur(self):
        return self.__hauteur

    
    
    
    #but: fonction qui fait bouger la plateforme
    #Entrée: event (touche que l'utilisateur presse, dans ce cas fleche droite ou gauche)
    def bouger_plateforme(self,event):
        touche=event.keysym

        #conditions pour que la plateforme ne sors pas du canvas

        # Si on se trouve au bord à droit, bouger que à gauche
        if self.__x + self.__largeur +10 > 1000:
            if touche == 'Right':
                pass
            elif touche == 'Left':
                self.__x -= 20
        
        # Si on se trouve au bord à gauche bouger que à droite 
        elif self.__x -10 < 0:
            if touche == 'Right':
                self.__x += 20
            elif touche == 'Left':
                pass
        
        #si on ne se trouve pas au bords, bouger librement
        else: 
            if touche == 'Right':
                self.__x += 20
            elif touche == 'Left':
                self.__x -= 20

        #actualiser les coordonées  
        self.__canvas.coords(self.__plateforme, self.__x, self.__y, self.__x+ self.__largeur, self.__y + self.__hauteur)
        

        

        

 




