
def compter_multiples_de_trois(liste):
    compteur = 0
    for nombre in liste:
        if nombre % 3 == 0:
            compteur += 1
    return compteur

# Liste donnée
L = [8, 24, 48, 2, 16]

# Compter le nombre de multiples de 3 dans la liste
resultat = compter_multiples_de_trois(L)
print("Le nombre de multiples de 3 dans la liste est :", resultat)

