# Lab 7 | Exercices 2 : Tuple et dictionnaire.

def histo_n(my_tup):
    ''' (tuple)->dict '''
    caract = {}
    for i in my_tup:
        caract[i] = caract.get(i, 0) + 1
    return caract

def sortnprint(dictionary):
    ''' (dict)->none '''
    for key in sorted(iter(dictionary.keys())):
        print(key, " : ", dictionary[key])
        
t = tuple(eval(input("Entrez seulement que des entiers et séparé(s) par des virgules ! : ")))
sortnprint(histo_n(t))
