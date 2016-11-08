# Lab 7 | Exercices 1 : Dictionnaire

def transform(chaine):
    ''' (string)->dict '''
    lettres = {}
    for i in chaine:
        lettres[i] = lettres.get(i, 0) + 1
    return lettres

def sortnprint(dictionary):
    ''' (dict)->none '''
    for key in sorted(iter(dictionary.keys())):
        print(key, " : ", dictionary[key])

print("Welcome ! This program has been created for one purpose ; sort anything you'll enter. \n Let's begin !!!")
chaine = input("Entrez un texte, message, etc. : ")
sortnprint(transform(chaine))


