#Jeronimo Gomez
#Daoud Hechaichi

#7/10/2023

#But: créer le jeu du casse briques, en utilisant tkinter et programation orientée objet

import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Casse Briques")
fenetre.geometry("500x400")

canvas = tk.Canvas(fenetre, width=500, height=400, bg="black")
canvas.pack()

button_quitter = tk.Button(canvas,text="quitter", command=fenetre.destroy, bg="red", fg="white")
button_quitter.pack()

fenetre.mainloop()


