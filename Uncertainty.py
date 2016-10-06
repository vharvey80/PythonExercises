from math import *

def AskUser():
    nbrValeur = 0
    Vals = []
    print("1) Calcul d'incertitude pour une : Addition ou Soustraction.")
    print("2) Calcul d'incertitude pour une : Multiplication ou Division.")
    reponse = ""
    while((reponse != "1") and (reponse != "2")):   
        reponse = input("Choisissez parmis les 2 options suivantes : ")
    if(reponse == "1"):
        print("\nAddition & soustraction")
        print("-------------------------\n")
        print("Équation : R = ± Ax ± By ± Cz [...], donc 3 variables")
        print("Incertitude : ∆R= √(A²∆x²) + (B²∆y²) + (C²∆z²)")
        print("∆ signifie incertitude.")
        val_R = int(input("\nQu'elle est la valeur de R ? : "))
        Vals.append(val_R)
        nbrValeur = int(input("Combien avez-vous de variable ? : "))
        Vals.append(nbrValeur)
        for i in range(nbrValeur):
            v_var = float(input("Entrez la valeur de la " + str(i + 1) + " variable (ex : A) : "))
            v_inc = float(input("Entrez la valeur de la " + str(i + 1) + " incertitude(ex : ∆x) : "))
            Vals.append(v_var)
            Vals.append(v_inc)
        CountUncertainty(Vals)
    elif(reponse == "2"):
        print("Multiplication & division")

def CountUncertainty(vals):
    u_sqrt = 0
    for i in range(2, (vals[1] + 1)):
       u_sqrt = u_sqrt + ((vals[i]**2) * (vals[i + 1]**2))
       uncertainty = sqrt(u_sqrt)
    if(uncertainty < 1):
        uncertainty = float(format(uncertainty, ".1f"))
    else :
        uncertainty = int(uncertainty)
    print("Donc ", vals[0], "±", uncertainty)
    
AskUser()
