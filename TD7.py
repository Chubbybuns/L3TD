# Exercice 1

montant = 1000
taux = 0.03
n = 10

for i in range(1, n + 1):
    montant = montant * (1 + taux)
    print(f"année {i}: {montant}")

# Exercice 2

t = [1, 2, 3, 4, 5, 6, 9]
nombre = 0
for element in t:
    if 5 <= element <= 10:
        nombre += 1
print(f"nombre d'éléments entre 5 et 10 : {nombre}")

# Exercice 3

t = [1, 2, 3, 4, 5, 6, 9]
somme = 0
for element in t:
    if 5 <= element <= 10:
        somme += element
print(f"somme des éléments entre 5 et 10 : {nombre}")

# Exercice 4

t = [1, 2, 3, 4, 5, 6, 9, 10, 20]
m = []

for element in t:
    if element >= 10:
        print(element)
        break

for element in t:
    if element >= 10:
        m.append(element)
if len(m) != 0:
    print(m[0])
else:
    print("Pas d'élément supérieur ou égal à 0")


# Exercice 5

t = [1, 2, 3, 4, 5, 6, 9]
n = []
for element in t:
    if element >= 10:
        n.append(element)

if len(n) != 0:
    print(n[-1])
else:
    print("Pas d'élément supérieur ou égal à 0")
