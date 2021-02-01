# Exercice 16 a)

mat = [[12, 1, 0],
       [1, 4, 1],
       [12, 1, 0],
       [1, 4, 1],
       [1, 0, 0],
       [1, 4, 1],
       [1, 0, 0],
       [1, 4, 1],
       [1, 0, 0]]
n = len(mat)
m = len(mat[0])

for index, line in enumerate(mat):
    for index2, element in enumerate(line):
        print(f"mat[{index},{index2}]: {element}")

# Exercice 16 b)

somme = 0
for line in mat:
    for element in line:
        somme += element

print(f"la somme de toutes les cases vaut : {somme}")

# Exercice 16 c)

somme2 = 0

for index, line in enumerate(mat):
    if index % 2 == 0:
        for element in line:
            somme2 += element
print(f"La somme des lignes paires est {somme2}")
