
def time_to_text(minutes):
    if minutes < 0:
        print("Veuillez entrer un nombre de minutes positif.")
    else:
        heures = minutes // 60  # Division entière pour obtenir le nombre d'heures
        minutes_restantes = minutes % 60  # Calcul du reste pour obtenir les minutes restantes

        if heures == 1:
            heures_str = "heure"
        else:
            heures_str = "heures"

        if minutes_restantes == 1:
            minutes_str = "minute"
        else:
            minutes_str = "minutes"

        print(f"{heures} {heures_str} et {minutes_restantes} {minutes_str}")

# Appel de la fonction time_to_text avec différentes valeurs
time_to_text(90)
time_to_text(120)
time_to_text(180)
time_to_text(60)
time_to_text(30)
