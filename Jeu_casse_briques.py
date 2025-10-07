
# -------------------------------------------------------
# Casse-Brique - Interface graphique seule
# Auteurs : Jeronimo Gomez, Daoud Hechaichi
# Date : 07/10/2023
# -------------------------------------------------------

import tkinter as tk

class CasseBriqueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Casse-Briques")
        self.root.geometry("600x500")
        self.root.config(bg="gray15")

        # --- Menu ---
        menubar = tk.Menu(self.root)
        menu_fichier = tk.Menu(menubar, tearoff=0)
        menu_fichier.add_command(label="Nouvelle partie", command=self.nouvelle_partie)
        menu_fichier.add_separator()
        menu_fichier.add_command(label="Quitter", command=self.root.quit)
        menubar.add_cascade(label="Fichier", menu=menu_fichier)
        self.root.config(menu=menubar)

        # --- Score et Infos ---
        frame_top = tk.Frame(self.root, bg="gray15")
        frame_top.pack(pady=10)

        self.label_score = tk.Label(frame_top, text="Score : 0", fg="white", bg="gray15", font=("Arial", 14))
        self.label_score.pack(side="left", padx=10)

        self.label_vies = tk.Label(frame_top, text="Vies : 3", fg="white", bg="gray15", font=("Arial", 14))
        self.label_vies.pack(side="right", padx=10)

        # --- Canevas principal ---
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="black", highlightthickness=2, highlightbackground="white")
        self.canvas.pack()

        # --- Boutons ---
        frame_bottom = tk.Frame(self.root, bg="gray15")
        frame_bottom.pack(pady=10)

        self.btn_start = tk.Button(frame_bottom, text="Démarrer", command=self.nouvelle_partie, font=("Arial", 12))
        self.btn_start.pack(side="left", padx=10)

        self.btn_quit = tk.Button(frame_bottom, text="Quitter", command=self.root.quit, font=("Arial", 12))
        self.btn_quit.pack(side="left", padx=10)

        # --- Éléments graphiques statiques ---
        self.creer_elements_visuels()

    def creer_elements_visuels(self):
        # Dessiner raquette
        self.raquette = self.canvas.create_rectangle(250, 370, 350, 380, fill="white")

        # Dessiner balle
        self.balle = self.canvas.create_oval(290, 350, 310, 370, fill="red")

        # Dessiner quelques briques en haut
        couleurs = ["red", "orange", "yellow", "green", "blue"]
        for i in range(5):
            for j in range(8):
                x1 = 10 + j * 70
                y1 = 10 + i * 25
                x2 = x1 + 60
                y2 = y1 + 20
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=couleurs[i], width=0)

    def nouvelle_partie(self):
        self.canvas.delete("all")
        self.creer_elements_visuels()
        self.label_score.config(text="Score : 0")
        self.label_vies.config(text="Vies : 3")


if __name__ == "__main__":
    root = tk.Tk()
    app = CasseBriqueApp(root)
    root.mainloop()