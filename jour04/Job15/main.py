
def tri_croissant(liste):
    # Tri par insertion
    for i in range(1, len(liste)):
        cle = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > cle:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = cle

def arrondir_et_trier(liste):
    liste_arrondie = []
    for nombre in liste:
        liste_arrondie.append(int(nombre + 0.5))
    
    tri_croissant(liste_arrondie)
    return liste_arrondie

# Liste initiale
liste_initiale = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Appeler la fonction pour arrondir et trier la liste
resultat = arrondir_et_trier(liste_initiale)

# Afficher le résultat
print("Liste arrondie et triée dans l'ordre croissant :", resultat)

