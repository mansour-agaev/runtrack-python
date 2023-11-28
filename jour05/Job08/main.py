
def my_sort(arr):
    count = 0  # Initialisation du compteur de coups
    n = len(arr)
    sorted = False  # Variable pour vérifier si la liste est triée

    while not sorted:
        sorted = True  # Supposons que la liste est triée
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Échanger les éléments adjacents
                count += 1  # Incrémenter le compteur de coups
                sorted = False  # La liste n'est pas encore triée
        n -= 1

    return arr, count

# Liste initiale à trier
liste_a_trier = [34, 22, 64, 11, 25, 90, 12]

# Appel de la fonction pour trier la liste et récupérer le nombre de coups nécessaires
resultat, coups_necessaires = my_sort(liste_a_trier)

# Affichage du nombre total de coups nécessaires pour trier la liste et de la liste triée
print("Nombre total de coups nécessaire pour trier la liste:", coups_necessaires)
print("Liste triée:", resultat)

