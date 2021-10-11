# Saisie des trois nombres
a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

# Comparaison et affichage du plus grand nombre
if a > b and a > c :
    print(f"{a} est le plus grand")
elif b > a and b > c :
    print(f"{b} est le plus grand")
elif c > a and c > b :
    print(f"{c} est le plus grand")


