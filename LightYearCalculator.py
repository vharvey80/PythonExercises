# Question 5 :

#a)

def CalculSeconde(annees):
    n_j = (float(str(annees.replace(",", "."))) * 365.26)
    n_h = n_j * 24
    n_m = n_h * 60
    n_s = n_m * 60
    return n_s

n_secondes = CalculSeconde(input("Entrez un nombre d'année(s) lumière : "))
print(format(n_secondes, ".2f") + " secondes")

#b)

def CalculDistance(secondes):
    n_km = (secondes * 300000)
    return n_km

n_kilometres = CalculDistance(n_secondes)
print(format(n_kilometres, ".2f") + "km")


#c)

def CalculDistanceEntreEtoiles(p_distance, d_distance):
    nseconde_1d = CalculSeconde(str(p_distance.replace(",", ".")))
    nkm_1d = CalculDistance(nseconde_1d)
    d_finale = nkm_1d
    nseconde_2d = CalculSeconde(str(d_distance.replace(",", ".")))
    nkm_2d = CalculDistance(nseconde_2d)
    d_finale += nkm_2d
    return d_finale

n_km_etoile = CalculDistanceEntreEtoiles(input("Entrez la distance de la première étoile : "), input("Entrez la distance de la deuxième étoile : "))
print(format(n_km_etoile, ".2f") + " km")
