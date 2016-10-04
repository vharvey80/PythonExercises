# Devoir 2 :
#1 :

def FindBMI(kg, m):
    n_kg = (float(str(kg.replace(",", "."))))
    n_m = (float(str(m.replace(",", "."))))
    bmi = (n_kg / (n_m**2))
    return bmi

tryagain = 'O'
while(tryagain == 'O'):
    realBMI = FindBMI(input("SVP entrez votre poids en kilogrammes : "), input("SVP entrez votre taille en mètres : "))
    print("Votre IMC est " + format(realBMI, ".2f"))
    if(realBMI < 18.5):
        print("Maigre")
    elif((realBMI >= 18.5) and (realBMI < 25)):
        print("Poids idéal")
    elif((realBMI >= 25) and (realBMI < 30)):
        print("Surpoids")
    elif(realBMI >= 30):
        print("Obésité")

    tryagain = '';

    while((tryagain != 'O') and (tryagain != 'N')):
        tryagain = input("Voulez-vous recommencer ? (O/N) : ")

print("Merci, au revoir !")
            
