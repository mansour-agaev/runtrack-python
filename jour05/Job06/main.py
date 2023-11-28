def distance_parcourue_semaine(nombre_marches, hauteur_marche):
    distance_jour = (nombre_marches * hauteur_marche * 2) / 100  # Conversion en mètres
    distance_semaine = distance_jour * 5 * 7  # 5 allers-retours par jour, 7 jours par semaine
    return distance_semaine

# Exemple d'utilisation avec 100 marches de 20 cm chacune
nombre_marches = 100
hauteur_marche = 20  # en cm

# Calcul de la distance parcourue par semaine
distance = distance_parcourue_semaine(nombre_marches, hauteur_marche)

# Affichage du résultat
print(f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance:.2f} m par semaine.")


