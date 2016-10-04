# Devoir 2 :
# 2 :

def displaybetween(a, b):
    for i in range (int(a), (int(b) + 1)):
        print(i)

print("Tous les entier entre deux entier (incluant ces deux entiers)")
displaybetween(input("SVP donnez la valeur du 1er entier : "),
               input("SVP donnez la valeur du 2e entier : "))
