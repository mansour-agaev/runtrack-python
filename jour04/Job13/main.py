
def supprimer_doublons(liste):
    liste_sans_doublons = []
    for element in liste:
        if element not in liste_sans_doublons:
            liste_sans_doublons.append(element)
    return liste_sans_doublons

# Liste initiale
liste_initiale = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Afficher la liste initiale
print("Liste initiale :", liste_initiale)

# Appeler la fonction pour supprimer les doublons
liste_sans_doublons = supprimer_doublons(liste_initiale)

# Afficher la liste après suppression des doublons
print("Liste sans doublons :", liste_sans_doublons)

