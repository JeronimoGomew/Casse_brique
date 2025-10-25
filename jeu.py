#Jeronimo Gomez et Daoud Hechaichi
#17/10/2025
#but: créer une classe jeu pour initialiser les variables du jeu, et pouvoir ré-initialiser facilement

from random import randint
from classe_plateforme import plateforme
from classes_balle import balle
from Classe_vies import Vies
from Brique import Brique, Brique_2vies, Brique_indestructible, Brique_rapide,Brique_lent
from Classe_scores import Score
from tkinter import Frame, Canvas,Button
from Classe_bonus import Bonus

class jeu :
    """""
    # Constructeur classe jeu
    # Entrées: fenetre tkinter ou sera mit le jeu
    """""
    def __init__(self,fenetre):
        self.__fenetre=fenetre
        
        # Frame du haut pour le score et les vies
        self.__FrameTop = Frame(self.__fenetre, bg="gray15", height=50)
        self.__FrameTop.pack(fill="x")
        
        
        # Canvas pour le jeu
        self.__zone_jeu = Canvas(self.__fenetre,bg='black',width=1000,height=500)
        self.__zone_jeu.pack()

        # Frame d'en bas pour les bouttons lancer, quitter et nouvelle partie
        self.__FrameBottom = Frame(self.__fenetre, bg="gray15", height=40)
        self.__FrameBottom.pack(side="bottom", fill="x")

        # bouton pour quitter la fenetre
        Boutton_Quitter = Button(self.__FrameBottom, text="Quitter",command = self.__fenetre.destroy)
        Boutton_Quitter.pack(side="right", pady=10, padx=10)
        # liaison de la touche Échap pour quitter le jeu
        self.__fenetre.bind("<Escape>", lambda event: self.__fenetre.destroy())

        # bouton pour commencer une nouvelle partie
        boutton_reinitier = Button(self.__FrameBottom,text="nouvelle partie",command=self.reinitier)
        boutton_reinitier.pack(side="left",pady=10,padx=10)
        self.__fenetre.bind("<R>", lambda event: self.reinitier()) 
        self.__fenetre.bind("<r>", lambda event: self.reinitier()) 



        # bouton pour lancer la balle et jouer
        Boutton_Demarrer = Button(self.__FrameBottom, text="Lancer la balle",command=self.Lancer)
        Boutton_Demarrer.pack(pady=10, padx=10)
        # liaison de la touche espace pour lancer la balle
        self.__fenetre.bind("<space>", lambda event: self.Lancer())

        


        #initialiser le jeu
        self.initialiser()

        
    def initialiser(self):
        """
        # initialiser les variables du jeu
        # Entrée: Rien
        # Sortie: Rien 
        """
        self.__plateforme = plateforme(self.__zone_jeu,600,450,140,20,"red")

        self.__gestion_vies = Vies(self.__FrameTop, nb_vies=3)
        self.__gestion_score = Score(self.__FrameTop, nb_points=0)
        self.__Bonus=Bonus(self.__plateforme,self.__fenetre)

        self.__ballejeu=balle(self.__zone_jeu,100,270,10,0,self.__fenetre,"red",90,self.liste_briques(),1,self.__plateforme,self.__Bonus)
        self.__ballejeu.suivre_plateforme(self.__plateforme)

    
    def reinitier(self):
        """""
        but: reinitier les variables du jeu
        Entrée: rien
        Sortie : rien
        """
        self.__zone_jeu.delete("all")#efface tout sur le canvas

        for widget in self.__FrameTop.winfo_children():#efface tout sur le Frame d'en haut (reinitialiser les vies et le score)
            widget.destroy()
        

        self.initialiser()#initalise tout à nouveau 

  
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

        for l in range(5):
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
                    
                    brique=Brique(self.__zone_jeu,x,y,largeur,hauteur)
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
                liste_br[index_liste]=Brique_2vies(self.__zone_jeu,x,y,largeur,hauteur)

            elif quel_brique==1:
                liste_br[index_liste]=Brique_indestructible(self.__zone_jeu,x,y,largeur,hauteur)
            
            elif quel_brique==2:
                liste_br[index_liste]=Brique_rapide(self.__zone_jeu,x,y,largeur,hauteur,self.__fenetre,self.__plateforme,self.__Bonus)

            elif quel_brique==3:
                liste_br[index_liste]=Brique_lent(self.__zone_jeu,x,y,largeur,hauteur,self.__fenetre,self.__plateforme,self.__Bonus)
         
        return liste_br
            

    def Lancer(self):
        """""
         fonction pour demarrer une nouvelle partie
         Entrées: aucune
         Sorties: aucune
         elle se declenche quand on appuie sur le bouton demarrer une nouvelle partie ou quand on appui sur le space
    
        """
        #verifions que la balle soit bien sur la plateforme
        if self.__ballejeu.suivre_plateforme(self.__plateforme)==True:

             
            difficulté=self.__ballejeu.get_difficulte()
            self.__ballejeu.mettre_a_jour_position_depuis_canvas()
            #recupere les coordonnées actuelles de la balle, sinon, le programme considère que se sont celles d'initialisation
            #de la classe quand on change sa vitesse
            self.__ballejeu.changer_vitesse(5+difficulté)
            #definir une vitesse qui dépend de combien de niveaux l'utilisateur a passé
            self.__ballejeu.mouvement(self.__plateforme,self.__gestion_vies,self.__gestion_score)
            #lancer le mouvement

        else:
            return





