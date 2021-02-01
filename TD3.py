# Exercice 11

u = 1
rang = 10
liste_premiers_termes = [u]
index = 0
while index < rang - 1:
    u = 2 * u + 1
    liste_premiers_termes.append(u)
    index += 1
print(liste_premiers_termes)

# Exercice 12

"""En vous inspirant de l’exercice précédent, calculez puis afficher le rang k du premier terme
de la suite U dont la valeur Uk dépasse 10000. 
"""

u = 1
liste_premiers_termes = [u]
index = 0
while liste_premiers_termes[-1] < 10000:
    u = 2 * u + 1
    liste_premiers_termes.append(u)
    index += 1
print(f"La suite atteint {liste_premiers_termes[-1]} en {index}")

# Exercice 13 a)

"""Entrez un nombre entier positif N : 36
Entrez un nombre entier positif M : 24
N | M
36 | 24
12 | 24
12 | 12 """

n = int(input("Entrez un nombre entier positif N :"))
m = int(input("Entrez un nombre entier positif M :"))
print(f"N | M\n{n}|{m}")
while n != m:
    if n > m:
        n = n - m
    else:
        m = m - n
    print(f"{n}|{m}")

# Exercice 13 b)

n2 = int(input("Entrez un nombre entier positif N :"))
m2 = int(input("Entrez un nombre entier positif M :"))
depart = [n2, m2]
while n2 != m2:
    if n2 > m2:
        n2 = n2 - m2
    else:
        m2 = m2 - n2

print(f"le PGCD de {depart[0]} et {depart[1]} vaut {n2}")
