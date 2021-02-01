# Exercice 1
print("j'affiche ce que je veux")

print("utiliser la combinaison suivante\n\npour passer a la ligne")

# Exercice 2

entier = 100
pi = 3.1416
mot = "test"

print(f"\nVoici un nombre entier : {entier}")
print(f"{pi} est un nombre décimal")
print(f"{mot} est une chaîne de caractères")

# Exercice 3

a = 1
b = 2
print(a, b)

a, b = b, a

print(a, b)

# Exercice 4

taux_tva = 0.2
montant_ttc = 220

montant_ht = montant_ttc/(1-taux_tva)

print(montant_ht)

# Exercice 5

prenom = input("Quel est ton prénom ?")
age = int(input("Quel est ton âge ?"))
taille = float(input("Quelle est ta taille en mètre ?"))
print("Ton prénom est", prenom)
print("Ton âge est", age)
print("Ta taille est", taille, "m")
