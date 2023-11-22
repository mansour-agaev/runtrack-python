
def verifie_nombre(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("négatif")
    else:
        print("Le nombre est égal à zéro")

# Appels de la fonction verifie_nombre avec différents paramètres
verifie_nombre(5)
verifie_nombre(-3)
verifie_nombre(0)
verifie_nombre(10)
