# Exercice 15 a)

t = [6, 12, 9, 1, 5, 10, 8, 3, 4, 13]
n = len(t)

nombre_valeurs_supérieurs_à_10 = 0
for element in t:
    if element > 10:
        nombre_valeurs_supérieurs_à_10 += 1
print(f"Le nombre d'éléments du tableau supérieurs à 10 est : {nombre_valeurs_supérieurs_à_10}")

# Exercice 15 b)
nombre_pairs = 0
for element in t:
    if element % 2 == 0:
        nombre_pairs += 1
print(f"Le nombre d'éléments pairs du tableau est : {nombre_pairs}")

# Exercice 15 c)

moyenne = sum(t) / len(t)
print(f"la moyenne des éléments du tableau est : {moyenne}")

# Exercice 15 d)

sorted_list = []

while t:
    minimum = t[0]  # arbitrary number in list
    for element in t:
        if element < minimum:
            minimum = element
    sorted_list.append(minimum)
    t.remove(minimum)

print(sorted_list)

for i in range(0, n-1):
    for j in range(i+1, n):
        if t[i] > t[j]:
            x = t[i]
            t[i] = t[j]
            t[j] = x
print(t)



