# Exercice 14 a)

t = [6, 12, 9, 1, 5, 10, 8, 3, 4, 13]
n = len(t)

for index, element in enumerate(t):
    print(f"t[{index}] : {element}")

# Exercice 14 b)

maximum = t[0]
for element in t:
    if maximum < element:
        maximum = element

print(f"le maximum du tableau est : {maximum}")

# Exercice 14 c)

minimum = t[0]
for element in t:
    if minimum > element:
        minimum = element

print(f"le maximum du tableau est : {minimum}")

# Exercice 14 d)

indice_minimum = t.index(minimum)
print(f"L’indice du minimum du tableau est : {indice_minimum}")

# Exercice 14 e)

somme = 0
for element in t:
    somme += element

print(f"La somme de tous les éléments du tableau : {somme}")
