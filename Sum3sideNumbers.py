# Lab 7 | Exercice 3 : Somme de trois nombre à la suite = 0.

def somme_de_trois(my_tuple):
    ''' (tuple)->boolean '''
    for i in range(len(my_tuple)):
        if((i + 2) < len(my_tuple)):
            somme = my_tuple[i] + my_tuple[i + 1] + my_tuple[i + 2]
            if(somme == 0):
               return True
        return False

t = tuple(eval(input("Entrez des chiffres uniquement et separé(s) par des virgules : ")))
print(somme_de_trois(t))
        
