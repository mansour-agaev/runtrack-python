
def tri_croissant(liste):
    for i in range(len(liste)):
        min_index = i
        for j in range(i + 1, len(liste)):
            if liste[min_index] > liste[j]:
                min_index = j
        # Échanger les éléments
        liste[i], liste[min_index] = liste[min_index], liste[i]

# Exemple d'utilisation
L = [7, 11, 4, 39, 2]

# Afficher la liste avant le tri
print("Liste avant le tri :", L)

# Appeler la fonction de tri
tri_croissant(L)

# Afficher la liste après le tri
print("Liste après le tri :", L)

