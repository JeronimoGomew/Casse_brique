import tkinter as tk

class Vies:
    """
    Classe pour gérer le nombre de vies du joueur
    et l'afficher sur un label Tkinter.
    """

    def __init__(self, frame_top, nb_vies=3, couleur_texte="white", bg="gray15"):
        """
        Initialise les vies avec un nombre de départ qui vaut 3 et crée le label associé.

        :param frame_top: frame dans laquelle le label sera affiché
        :param nb_vies: nombre de vies initial
        :param couleur_texte: couleur du texte du label
        :param bg: couleur de fond du label
        """
     
        
        self.nb_vies = nb_vies
        self.var_vies = tk.StringVar()
        self.var_vies.set(f"Vies : {self.nb_vies}")

        self.label_vies = tk.Label(
            frame_top,
            textvariable=self.var_vies,
            fg=couleur_texte,
            bg=bg,
            font=("Arial", 14, "bold")
        )
        self.label_vies.pack(side="right", padx=20, pady=10)

    def perdre_vie(self):
        """Retire une vie et met à jour l'affichage."""
        if self.nb_vies > 0:
            self.nb_vies -= 1
        self.var_vies.set(f"Vies : {self.nb_vies}")



    def reset(self, nb_vies=3):
        """Réinitialise le compteur de vies."""
        self.nb_vies = nb_vies
        self.var_vies.set(f"Vies : {self.nb_vies}")


        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test affichage des vies")
    root.geometry("600x100")
    root.config(bg="gray20")

    frame = tk.Frame(root, bg="gray15", height=50)
    frame.pack(fill="x")

    gestion_vies = Vies(frame)
    root.mainloop()