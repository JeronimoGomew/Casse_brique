"""Daoud Hechaichi et Jeronimo Gomez"""
"18/10/2025"
"but: créer la classe vie avec une structure de pile"

from tkinter import StringVar,Label

class Vies:
    """
    partie qui gerent  les vies du joueur sous forme d'une pile.
    les vies snt representées par des coeurs en emoji (❤️) et la pile est mise à jour automatiquement.
    """

    def __init__(self, frame_top, nb_vies, couleur_texte="white", bg="gray15"):
        """
        Initialise la pile de vies avec un nombre donné,ici 3,  et configure le label d'affichage

        
        parametre nb_vies: Nombre initial de vies
        parametre couleur_texte: Couleur du texte du label
        parametre bg: Couleur de fond du label
        """
        self.nb_vies_initial = nb_vies
        self.pile_vies = ["❤️" for _ in range(nb_vies)]  # pile de vies qui sont des coeurs emoji
        self.var_vies = StringVar()
        self.var_vies.set(f"Vies : {' '.join(self.pile_vies)}")

        self.label_vies = Label(
            frame_top,
            textvariable=self.var_vies,
            fg=couleur_texte,
            bg=bg,
            font=("Arial", 14, "bold")
        )
        self.label_vies.pack(side="right", padx=20, pady=10)


    def perdre_vie(self):
        """
       enleve une vie a la pile donc au joueur si possiblke et met a jour l'affichage en consequence
        """
        if self.pile_vies:
            self.pile_vies.pop()
        self.var_vies.set(f"Vies : {' '.join(self.pile_vies)}")

    
    def getnbvies(self):
        return len(self.pile_vies)


