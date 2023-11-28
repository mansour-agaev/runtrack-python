
def somme_valeurs_paires(liste):
    somme = 0
    for nombre in liste:
        if nombre % 2 == 0:  # Vérifie si le nombre est pair
            somme += nombre
    return somme

# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# Calcul de la somme des valeurs paires dans la liste
resultat = somme_valeurs_paires(L)
print("La somme des valeurs paires dans la liste est :", resultat)

