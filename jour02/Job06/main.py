
def trouver_nombres_premiers(maximum):
    # Initialisation d'une liste pour marquer les nombres non premiers
    sieve = [True] * (maximum + 1)
    sieve[0], sieve[1] = False, False  # 0 et 1 ne sont pas premiers

    # Marquer les multiples des nombres premiers comme non premiers
    for i in range(2, int(maximum**0.5) + 1):
        if sieve[i] == True:
            for j in range(i * i, maximum + 1, i):
                sieve[j] = False

    # Afficher les nombres premiers
    print("Les nombres premiers jusqu'à", maximum, "sont :")
    for i in range(2, maximum + 1):
        if sieve[i] == True:
            print(i, end=" ")

# Appel de la fonction pour afficher les nombres premiers jusqu'à 1000
trouver_nombres_premiers(1000)
