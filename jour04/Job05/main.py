
def remplacer_element(liste):
    liste[3] = liste[2] + liste[4]
    return liste

# Création de la liste d'entiers
L = [1, 2, 3, 4, 5]

# Affichage de la deuxième valeur de la liste
deuxieme_valeur = L[1]
print(deuxieme_valeur)

# Remplacement de L[3] par la somme des cases voisines L[2] & L[4]
L = remplacer_element(L)
print(L)

# Affichage de la dernière valeur de la liste
derniere_valeur = L[-1]
print(derniere_valeur)
