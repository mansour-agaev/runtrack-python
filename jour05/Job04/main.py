
def draw_carpet_with_diagonal(n):
    for i in range(n+1):
        for j in range(n+1):
            if i == j or i == 0 or j == 0 or i == n or j == n:
                print("*", end=" ")  # Caractère pour la diagonale
            else:
                print(" ", end=" ")  # Espaces pour le reste du tapis
        print()

# Appel de la fonction avec une taille de 10
draw_carpet_with_diagonal(10)



