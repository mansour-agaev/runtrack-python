
def affiche_aliments(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine, navet")
    else:
        print("Aucun aliment correspondant aux critères donnés.")

# Appels de la fonction affiche_aliments avec différents paramètres
affiche_aliments("fruits", "hiver")
affiche_aliments("fruits", "ete")
affiche_aliments("legume", "hiver")
affiche_aliments("legume", "ete")
affiche_aliments("autre", "autre")
