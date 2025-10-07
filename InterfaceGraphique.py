import tkinter as tk
import classes_balle as b


MaFenetre = tk.Tk()
MaFenetre.title ("Jeu du casse-briques")
MaFenetre.geometry("1000x600")
MaFenetre.config(bg="gray20")


FrameTop = tk.Frame(MaFenetre, bg="gray15", height=50)
FrameTop.pack(fill="x")

Canvas = tk.Canvas(MaFenetre, bg="black", width=1000, height=500)
Canvas.pack()

LabelScore = tk.Label(FrameTop, text="Score : 0", fg="white", bg="gray15", font=("Arial", 14, "bold"))
LabelScore.pack(side="left", padx=20, pady=10)

LabelVies = tk.Label(FrameTop, text="Vies : 3", fg="white", bg="gray15", font=("Arial", 14, "bold"))
LabelVies.pack(side='right', padx=20, pady=10)


FrameBottom = tk.Frame(MaFenetre, bg="gray15", height=40)
FrameBottom.pack(side="bottom", fill="x")

Boutton_Quitter = tk.Button(FrameBottom, text="Quitter",command = MaFenetre.destroy)
Boutton_Quitter.pack(side="right", pady=10, padx=10)




Boutton_Demarrer = tk.Button(FrameBottom, text="Demarrer une nouvelle partie")
Boutton_Demarrer.pack(side="left", pady=10, padx=10)


balle1=b.balle(Canvas,100,200,10,5,MaFenetre,"red",10)
balle1.mouvement()


MaFenetre.mainloop()

