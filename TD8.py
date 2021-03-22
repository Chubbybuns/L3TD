# exercice 1
import math

# question 1


def f(x):
    return x*x


print(f(3))

# question 2 et 3


def g(x):
    return 2*math.sqrt(1-x*x)


print(g(1))
print(g(0))


def integrale(f, a, b, n):
    h = (b-a)/n  # largeur de chaque rectangle
    som = 0
    for i in range(0, n):
        x = a+i*h
        som = som+f(x)*h
    return som


print(integrale(g, -1, 1, 10))
print(integrale(g, -1, 1, 100))
print(integrale(g, -1, 1, 1000))
print(integrale(g, -1, 1, 10000))
print(integrale(f, -1, 2, 10000))


# exercice 3
luo = [[4, 9, 2],
       [3, 5, 7],
       [8, 1, 6]]

durer = [[16, 3, 2, 13],
         [5, 10, 11, 8],
         [9, 6, 7, 12],
         [4, 15, 14, 1]]

m1 = [[2, 3],
      [4, 5]]

# m = luo  #ou durer ou m1
# m = durer
m = m1
n = len(m)

# somme des éléments sur une ligne :

valeursomme = []

for i in range(0, n):
    # (ligne i):
    S = 0
    for k in range(0, n):
        S = S+m[i][k]
    print("ligne", i, "la somme vaut :", S)
    valeursomme.append(S)  # n sommes

for k in range(0, n):
    # colonne k):
    S = 0
    for i in range(0, n):
        S = S+m[i][k]
    print("colonne", k, "la somme vaut :", S)
    valeursomme.append(S)  # n sommes

S = 0
for i in range(0, n):
    S = S+m[i][i]
print("diag. principale, la somme vaut :", S)
valeursomme.append(S)  # 1 somme

S = 0
for i in range(0, n):
    S = S+m[i][n-i-1]
print("diag. secondaire, la somme vaut :", S)
valeursomme.append(S)  # 1 somme

# le tableau contient 2n+2 éléments
# indices : 0 à 2n+1
# il faut voir s'il sont tous égaux ou pas

# on suppose qu'on a un carré magique par défaut :
estmagique = 1
i = 1
while i <= 2*n+1 and valeursomme[0] == valeursomme[i]:
    i = i+1
print(i)

if i != 2*n+2:
    estmagique = 0

# on met tous les éléments de m
# dans un tableau t à une dimension:
t = []
for i in range(0, n):
    for k in range(0, n):
        t.append(m[i][k])

u = sorted(t)
# u contient n*n éléments
for i in range(0, n*n-1):
    # tester si deux élements consécutifs sont égaux
    if u[i] == u[i+1]:
        estmagique = 0

if estmagique == 1:
    print("carré magique")
else:
    print("pas un carré magique")

# exercice 2

A = [[1, 2],
     [3, 4],
     [5, 6]]
n = len(A)
m = len(A[0])

C = [[0 for j in range(0, n)] for i in range(0, m)]

for i in range(0, m):
    for j in range(0, n):
        C[i][j] = A[j][i]

print("C=", C)
