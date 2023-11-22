
string = "abcdefghijklmnopqrstuvwxyz" * 10
rows = 10  # Nombre de lignes de la pyramide
max_chars = 1  # Nombre maximum de caractères à afficher par ligne
current_char = 0  # Index pour parcourir la chaîne

for i in range(rows):
    line = string[current_char:current_char + max_chars]
    print(line.center(rows * 2))  # Affichage centré
    current_char += max_chars
    max_chars += 2
