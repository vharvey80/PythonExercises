# Devoir 4 | Question 1
''' Créez une fonction en Python appelée ajoute, qui prend une matrice et qui
modifie la matrice en ajoutant 1 à tous les éléments. Créez une autre fonction Python appelée
ajoute_V2, qui prend une matrice et qui retourne une nouvelle matrice contenant les valeurs de la
matrice donnée comme paramètre incrémentée avec 1, sans la modifier. '''

import copy

def loopInMatrix(m):
    ''' (2D list) -> None
    Fonction qui fait le tour d'une matrice et incrémente la valeur de celle-ci.'''
    for row in range(len(m)):
        for col in range(len(m[row])):
            m[row][col] += 1

def add(m):
    ''' (2D list) -> None
    Fonction qui incrémente les valeurs de la matrice de 1 (+1).'''
    loopInMatrix(m)
    print("Après l'exécution de la fonction add, la matrice est :")

def add_V2(m):
    ''' (2D list) -> 2D list
    Fonction qui fait une copie de la première matrice et incrémente ces valeurs de 1 (+1) sans modifier l'originale.'''
    n_m = copy.deepcopy(m)
    loopInMatrix(n_m)
    print("Une nouvelle matrice a été créée avec add_V2 :")
    return n_m

def displayOriginalMatrix(m):
    ''' (2D list) -> None
    Fonction qui fait afficher la matrice originale après l'incrémentation.'''
    print("Après l'exécution de la fonction add_V2, la matrice initiale est:")
    print(m)

def askuser(m):
    ''' (2D list) -> None
    Fonction qui demande à l'usager d'entrez les valeurs de sa matrice.'''
    print("Entrez les éléments de la matrice avec espaces entre les colonnes.")
    print("Une rangée par ligne, et une ligne vide à la fin (Doule enter).")
    x = [1]  # Matrice temporaire
    while(x[0] != ''):
        x = input().split(" ")
        if(x[0] != ''):
            for i in range(len(x)):
                    x[i] = int(x[i])
            m.append(x)
    print("La matrice est :")
            
m = [] # Matrice principale
askuser(m)
print(m)
add(m)
print(m)
new_m = add_V2(m) # Création d'une nouvelle matrice
print(new_m)
displayOriginalMatrix(m)
