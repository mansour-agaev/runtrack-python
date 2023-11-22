
def verifie_pair_impair(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            print(f"Le nombre {nombre} est pair.")
        else:
            print(f"Le nombre {nombre} est impair.")
    else:
        print("Veuillez entrer un nombre entier positif.")

# Appels de la fonction verifie_pair_impair avec différentes valeurs
verifie_pair_impair(5)
verifie_pair_impair(12)
verifie_pair_impair(-3)
verifie_pair_impair("abc")
verifie_pair_impair(8.5)

