# Convertisseur de livres en onces / onces en livres

def Convertisseur(n_lbs, n_onces, c_lbs, c_onces):
    rn_lbs = float(format(float(n_lbs.replace(",", ".")), '.1f'))
    rn_onces = float(format(float(n_onces.replace(",", ".")), '.1f'))
    k_lbs = (rn_lbs / c_lbs)
    k_onces = (rn_onces / c_onces)
    kilogrammes = (k_lbs + k_onces)
    return kilogrammes

print("Convertisseur de livre(s) et d'onces en kilogrammes ! \n")

n_lbs = input("Entrez un nombre de livre : ")
n_onces = input("Entrez un nombre d'onces : ")
c_lbs = 2.20462 # Valeur de convertion
c_onces = 35.274 # Valeur de convertion

k_final = format(Convertisseur(n_lbs, n_onces, c_lbs, c_onces), '.4f')
print(k_final + " kilogrammes")

