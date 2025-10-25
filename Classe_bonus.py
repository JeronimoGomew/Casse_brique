"""""
Jeronimo Gomez, Daoud Hechaichi
25/10/2025
but: créer la gestion des bonus sous forme de file
a améliorer: gestioner des bonus autre que de vitesse sur la plateforme (comme des bonus sur la taille de la platforme)
"""""

class Bonus:


    def __init__(self,plateforme,fenetre):
        self._file_bonus = []
        self._plateforme = plateforme
        self._bonus_actif = False
        self._fenetre = fenetre
        self._vitesse_init_plateforme=20


    def ajouter_bonus(self,dif_vitesse):
        """"
        entrée: dif_vitesse (int) (c'est le delta vitesse, qu'on ajoutera à la vitesse initiale)
        sortie:rien

        cette fonction ajoute un bonus dans la file, si il n'y a pas de bonus actif, elle l'execute
        """
        self._file_bonus.append(dif_vitesse)

        if self._bonus_actif == False:
            self.traiter_bonus()
    

    def traiter_bonus(self):
        """"
        entrée: rien
        sortie: rien 

        cette fonction change la vitesse de la plateforme, en ajoutant a la vitesse initiale la première
        valeur de la file_bonus
        après de 6 secondes, elle fait appel a la fonction finir_bonus
        """
    
        self._bonus_actif=True

        
           

        self._plateforme.changer_pas(self._vitesse_init_plateforme+self._file_bonus[0])
        self._fenetre.after(6000,self.finir_bonus,self._vitesse_init_plateforme)
    

    def finir_bonus(self,vitesse_init):
        """"
        entrée: vitesse_init (int) vitesse initiale de la platforme
        sortie: rien

        cette fonction reinitialise la vitesse de la plaforme, pop la première valeur de la file
        et execute la prochaine, si il y en a.
        """
        self._plateforme.changer_pas(vitesse_init)
        self._file_bonus.pop(0)
        self._bonus_actif = False

        if self._file_bonus:  # seulement si un bonus n'est pas vide
            self.traiter_bonus()
                





