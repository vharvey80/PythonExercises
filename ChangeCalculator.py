# Question 2 & 4:
# N.B. Le TA m'a confirmé que ce n'était pas grave si j'avais fais la question 2 comme la 4

def CalculChange(d):
    r_dollar = float(format(float(d.replace(",", ".")), ".2f"))
    n_25 = n_10 = n_5 = n_1 = 0
    dollars = (r_dollar * 100)
    n_25 = dollars // 25
    dollars = dollars % 25
    if(dollars > 0):
        n_10 = dollars // 10
        dollars = dollars % 10
        if(dollars > 0):
            n_5 = dollars // 5
            dollars = dollars % 5
            if(dollars > 0):
                n_1 = dollars // 1

    n_total = n_25 + n_10 + n_5 + n_1            
    print ("# de 25 : " + str(n_25) + "\n# de 10 : " + str(n_10) + "\n# de 5 : " + str(n_5) + "\n# de 1 : " + str(n_1))
    return n_total 

print("Machine à calculer le change ! \n")

n_total = CalculChange(input("Entrez un nombre de dollar : "))
print("Le nombre de pièce minimum que le caissier devra rendre est : " + str(int(n_total)))
