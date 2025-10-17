from tkinter import StringVar,Label

class Vies:
    """
    partie qui gerent du joueur les vies du joueur sous forme d'une pile de cœurs affichée dans une interface Tkinter.
    Chaque vie est représentée par un cœur (❤️) et la pile est mise à jour automatiquement.
    """

    def __init__(self, frame_top, nb_vies, couleur_texte="white", bg="gray15"):
        """
        Initialise la pile de vies avec un nombre donné,ici 3,  et configure le label d'affichage

        
        param nb_vies: Nombre initial de vies
        param couleur_texte: Couleur du texte du label
        param bg: Couleur de fond du label
        """
        self.nb_vies_initial = nb_vies
        self.pile_vies = ["❤️" for _ in range(nb_vies)]  # La pile de vies, chaque vie est un cœur
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

    def ajouter_vie(self):
        """
        Ajoute une vie à la pile
        Met à jour l'affichage en conséquence
        """
        self.pile_vies.append("❤️")
        self.var_vies.set(f"Vies : {' '.join(self.pile_vies)}")

    def reset(self):
        """
        Remet la pile de vies à son état initial
        Met à jour l'affichage
        """
        self.pile_vies = ["❤️" for _ in range(self.nb_vies_initial)]
        self.var_vies.set(f"Vies : {' '.join(self.pile_vies)}")
    
    def getnbvies(self):
        return len(self.pile_vies)


