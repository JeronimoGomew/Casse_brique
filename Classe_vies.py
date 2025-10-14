import tkinter as tk

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
        self.var_vies = tk.StringVar()
        self.var_vies.set(f"Vies : {' '.join(self.pile_vies)}")

        self.label_vies = tk.Label(
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


# Bloc de test pour visualiser la classe Vies
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test affichage des vies")
    root.geometry("600x200")
    root.config(bg="gray20")

    # Frame supérieure
    frame = tk.Frame(root, bg="gray15", height=50)
    frame.pack(fill="x")

    # Canvas pour tester l'affichage du Game Over
    canvas = tk.Canvas(root, width=560, height=300, bg="black")
    canvas.pack(pady=20)

    # Création du gestionnaire de vies
    gestion_vies = Vies(frame, nb_vies=3)

    # Boutons de test
    tk.Button(frame, text="-1 Vie", command=gestion_vies.perdre_vie,
              bg="gray30", fg="black").pack(side="left", padx=10)
    tk.Button(frame, text="+1 Vie", command=gestion_vies.ajouter_vie,
              bg="gray30", fg="black").pack(side="left", padx=10)
    tk.Button(frame, text="Reset Vies", command=gestion_vies.reset,
              bg="gray30", fg="black").pack(side="left", padx=10)

    tk.Button(frame, text="Quitter", command=root.destroy,
              bg="gray30", fg="black").pack(side="left", padx=10)

    root.mainloop()
    root.quit()