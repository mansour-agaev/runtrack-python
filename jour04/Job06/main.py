
def echanger_premiere_derniere(liste):
    if len(liste) > 0:
        liste[0], liste[-1] = liste[-1], liste[0]
    return liste

# Liste initiale
liste = [1, 2, 3, 4, 5]

# Affichage de la liste initiale
print(liste)

# Échange des valeurs de la première et de la dernière case
resultat_attendu = echanger_premiere_derniere(liste)
print(resultat_attendu)
