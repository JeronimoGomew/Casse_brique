

"""
-------------------------------------------------------
Casse-Brique - Interface graphique seule
Auteurs : Jeronimo Gomez, Daoud Hechaichi
Date : 07/10/2023
-------------------------------------------------------

-------------------------------------------------------
À propos du Canvas
-------------------------------------------------------
Le Canvas est la scène principale de notre jeu.
C’est là que se passe toute l’action : la balle, la raquette, les briques...

Dans notre jeu du casse-brique, on lui donne :
  • un fond sombre ("gray12") pour offrir un aspect moins agressif pour les yeux,
  • un contour blanc pour délimiter clairement la zone de jeu,
  • une taille fixe (560x360) pour garder une mise en page propre.

Le Canvas est entouré de deux frames principales :
  • une première en haut pour afficher le score et les vies restantes,
  • une deuxième en bas pour les boutons de contrôle (Démarrer, Quitter).
-------------------------------------------------------
"""

import tkinter as tk

class CasseBriqueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Casse-Briques")
        self.root.geometry("600x500")
        self.root.config(bg="gray20")

        frame_infos = tk.Frame(self.root, bg="gray20")
        frame_infos.pack(pady=10)

        self.btn_score = tk.Button(frame_infos, text="Score : 0", font=("Arial", 14),
                                   state=tk.DISABLED, disabledforeground="white",
                                   bg="gray35", activebackground="gray35", relief=tk.FLAT)
        self.btn_score.pack(side="left", padx=10)

        self.btn_vies = tk.Button(frame_infos, text="Vies : 3", font=("Arial", 14),
                                  state=tk.DISABLED, disabledforeground="white",
                                  bg="gray35", activebackground="gray35", relief=tk.FLAT)
        self.btn_vies.pack(side="left", padx=10)

        self.canvas = tk.Canvas(self.root, width=560, height=360, bg="gray12",
                                highlightthickness=2, highlightbackground="white")
        self.canvas.pack(padx=20, pady=10)

        frame_commandes = tk.Frame(self.root, bg="gray20")
        frame_commandes.pack(pady=10)

        self.btn_start = tk.Button(frame_commandes, text="Démarrer", font=("Arial", 12),
                                command=self.demarrer_partie,
                                bg="gray35", fg="black",
                                activebackground="gray40", activeforeground="black",
                                relief=tk.FLAT)
        self.btn_start.pack(side="left", padx=10)

        self.btn_quit = tk.Button(frame_commandes, text="Quitter", font=("Arial", 12),
                                  command=self.root.destroy,
                                  bg="gray35", fg="black",
                                  activebackground="gray40", activeforeground="black",
                                  relief=tk.FLAT)
        self.btn_quit.pack(side="left", padx=10)

    """
    -------------------------------------------------------
    Fonction : demarrer_partie
    -------------------------------------------------------
    Cette fonction gère le lancement d’une nouvelle partie.

    Étape 1 :
        Elle efface entièrement le canevas pour supprimer
        tout élément graphique précédemment affiché (briques,
        balle, raquette…).

    Étape 2 :
        À cet endroit, seront ajoutées plus tard les actions de
        réinitialisation du score, du nombre de vies et des éléments
        visuels du jeu.

    Étape 3 :
        Lorsque la logique du jeu sera complète, cette fonction
        deviendra le point de départ pour initialiser la boucle
        principale (mouvements, collisions, etc.).

    En résumé :
        Cette méthode remet le canevas à zéro à chaque démarrage
        afin de garantir un état propre avant le lancement d’une
        nouvelle partie.
    -------------------------------------------------------
    """
    def demarrer_partie(self):
        self.canvas.delete("all")



if __name__ == "__main__":
    root = tk.Tk()
    app = CasseBriqueApp(root)
    root.mainloop()