# 🎮 Projet : Casse-Brique Python  

![Made with Python](https://forthebadge.com/images/badges/made-with-python.svg)
![Built with Love](https://forthebadge.com/images/badges/built-with-love.svg)

Un jeu de casse-brique réalisé en **Python** avec **Matplotlib**, **PIL**, **Tkinter** et **Random** développé par **Daoud Hechaïchi** et **Jeronimo Gomez** en classe de  **3ETI, CPE Lyon**.  

Le projet est crée en Programmation Orientée Objet. Il est crée avec un fichier par classe et une interface graphique complète avec des éléments visuels comme une tortue 🐢 et un lapin 🐇 animés pour des bonus... ou malus 😈.

## 🎯 Règles du jeu

- Le joueur deplace une raquette en bas de l’écran et doit renvoyer la balle pour détruire toutes les briques.  
- Chaque fois que toutes les briques seront detruite un diamant 💎 sera gagné et la partie est gagnée 🎉..  
- Si la balle tombe en bas de la fenetre🪟, le joueur perd une vie ❤️.  
- Si le joueur perd toutes ses vies, la partie est terminée 💀.  
- Certains éléments visuels (🐢 Tortue, 🐇 Lapin) provenant de certaines briques peuvent apporter des **bonus** ou **malus** au joueur.  






## 🧮 Structures de données (files, piles...)

Des differentes structures de données sont utilisées:

- **Pile de vies (Stack)** → implémentée dans `Classe_vies.py` => à chaque defaite on enlève un coeur ❤️. 
- **Pile de score (Stack)** → dans `Classe_scores.py` => à chaque fois que toutes les briques sont detruites, un diamant 💎 est gagné. 
  





## 🚀 Fonctionnalités principales

- Mouvement realiste de la balle, rebonds sur les murs et la raquette suivant les lois d'optique de Descartes.  
- Destruction des briques avec mise à jour du score 💎 lorsque toutes les briques sont detruites.     
- Gestion dynamique des vies ❤️.     
- Bouton **nouvelle partie / Rejouer** pour relancer une partie sans redémarrer le jeu.  
- Interface graphique sous Tkinter.   
- Ajout d’éléments visuels : **tortue**🐢 et **lapin** 🐇 sur le canvas.   
- Programation orientée objet.  


## ⌨️ Raccourcis clavier 💡

Plusieurs raccourcis clavier ont été ajoutés pour pouvoir jouer sans souris :

| Touche | Action |
|:-------|:--------|
| **Espace** ⎵ | Lance la balle (équivalent du bouton *Démarrer/Rejouer*) |
| **R** 🔁 | Redémarre une nouvelle partie |
| **Échap** ⎋ | Quitte le jeu et ferme la fenêtre Tkinter |

 

## 🧠 Structure du projet
```bash
Casse_brique-1/
│
├── Programme_principal.py   → Point d’entrée principal du jeu (lance l’interface)
├── jeu.py                   → Logique de jeu, gestion du canvas, interactions, initialisation des variables (balle, raquette...)
├── classes_balle.py         → Classe gérant la balle (mouvement, collisions, rebonds)
├── classe_plateforme.py     → Classe pour la raquette du joueur
├── Brique.py                → Classe modélisant les briques
├── Classe_vies.py           → Gestion des vies ❤️
├── Classe_scores.py         → Gestion du score 💎
├── TORTUE.gif               → Sprite de la tortue 🐢 (élément décoratif ou animation)
├── LAPIN.gif                → Sprite du lapin 🐇 (élément décoratif ou animation)
└── README.md                → Présentation complète du projet

```

## ⚙️ Installation et exécution

Pour lancer le jeu **Casse-Brique Python**, suis simplement ces étapes 👇



### 🧩 1️⃣ Cloner le dépôt

Ouvrez votre terminal et exécutez ces commandes pour récupérer le projet :

```bash
git clone https://github.com/JeronimoGomew/Casse_brique.git
cd Casse_brique
```

### 🚀 2️⃣ Lancer le jeu

Une fois dans le dossier du projet, exécutez le fichier principal :

```bash
python Programme_principal.py