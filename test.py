from random import randint






dico_briques = {0: list(range(0, 8)),1: list(range(0, 8)),2: list(range(0, 8)),3: list(range(0,8))}
liste_br = []


briques_spéciaux=[]
briques2_vies=[]
briques_indestructible=[]
briques_rapides=[]
briques_lents=[]

for l in range(5):
    ligne_aleatoire = randint(0,3) 
    colonne_aleatoire = randint(0,(len(dico_briques[ligne_aleatoire])-1))

    
    briques_spéciaux.append([ligne_aleatoire,dico_briques[ligne_aleatoire][colonne_aleatoire]])

    dico_briques[ligne_aleatoire].pop(colonne_aleatoire)
    
    print(briques_spéciaux)

for l in range (10):
    print(l%5)
    
    



