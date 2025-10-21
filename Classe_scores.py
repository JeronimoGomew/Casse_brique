import tkinter as tk

class Score:
    """
    Cette classe s'occupe du  score 
    À chaque point gagné un diamant +1 s'ajoute à l'affichage
    À chaque point perdu un diamant -1 s'enlève de l'affichage 
    on peut aussi remettre le score à zéro
    """

    def __init__(self, frame_top, nb_points=0, couleur_texte="white", bg="gray15"):
        """
        Initialise le score avec un nombre donné, ici 0, et configure le label d'affichage
        param nb_points: Nombre initial de points
        param couleur_texte: Couleur du texte du label
        param bg: Couleur de fond du label      
        """
        self.nb_points = nb_points
        self.nb_niveaux_complétés = 0
        self.pile_score = []#"💎" for _ in range(self.nb_niveaux_complétés)]  # Un diamant par point
        self.var_score = tk.StringVar()
        self.var_score.set(f"Score : {self.nb_points} {' '.join(self.pile_score)}")

        self.label_score = tk.Label(
            frame_top,
            textvariable=self.var_score,
            fg=couleur_texte,
            bg=bg,
            font=("Arial", 14, "bold")
        )
        self.label_score.pack(side="left", padx=20, pady=10)

    def ajouter_point(self):
        """On ajoute un point, donc un diamant à l'affichage"""
        self.nb_points += 1
        self.var_score.set(f"Score : {self.nb_points} {' '.join(self.pile_score)}")
    
    def ajouter_niveau(self):
        self.pile_score.append("💎")
        self.var_score.set(f"Score : {self.nb_points} {' '.join(self.pile_score)}")


    def retirer_point(self):
        """on enelève un point, donc un diamant à l'affichage si possible c'est a dire si il reste des diamants a enlver """
        if self.pile_score:
            self.pile_score.pop()
        self.var_score.set(f"Score : {len(self.pile_score)} {' '.join(self.pile_score)}")

    def reset(self):
        """On remet le score à zéro et on met à jour l'affichage"""
        self.pile_score = ["💎" for _ in range(self.nb_points_initial)]
        self.var_score.set(f"Score : {len(self.pile_score)} {' '.join(self.pile_score)}")

