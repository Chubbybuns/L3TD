# Exercice 6

nombre = int(input("Entrez un nombre entier :"))
if nombre % 2 == 0:
    print("Votre nombre est pair ")
else:
    print("Votre nombre est impair")

# Exercice 7

"""Généralisez l'exercice précédent : saisir un nombre entier P et un nombre entier Q pour dire
si Q divise P ou non. 
"""

p = int(input("Entrez un nombre entier p:"))
q = int(input("Entrez un diviseur entier q:"))
if p % q == 0:
    print("q divise p")
else:
    print("q ne divise pas p")

# Exercice 8

a = int(input("Entrez un premier nombre :"))
b = int(input("Entrez un second nombre :"))

if a > b:
    print(f"Maximum : {a}\nMinimum : {b}")
else:
    print(f"Maximum : {b}\nMinimum : {a}")

# Exercice 9

nombre = int(input("Entrez un nombre entier :"))
liste_diviseurs = []

print(f"Les diviseurs de {nombre} sont :")
for i in range(1, nombre + 1):
    if nombre % i == 0:
        liste_diviseurs.append(i)
print(liste_diviseurs)

# Exercice 10 a)

N = int(input("Entrez un nombre entier positif N :"))
M = int(input("Entrez un nombre entier positif M :"))

liste_diviseurs_n = []
liste_diviseurs_m = []

for i in range(1, N + 1):
    if N % i == 0:
        liste_diviseurs_n.append(i)

for i in range(1, M + 1):
    if M % i == 0:
        liste_diviseurs_m.append(i)

liste_diviseurs_communs = list(set(liste_diviseurs_n).intersection(liste_diviseurs_m))
print(liste_diviseurs_communs)

# Exercice 10 b)

max_diviseurs_communs = max(liste_diviseurs_communs)
print(max_diviseurs_communs)

