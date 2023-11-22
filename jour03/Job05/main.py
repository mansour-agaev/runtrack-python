def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Gérer la division par zéro
        if num2 == 0:
            return "Erreur : Division par zéro impossible."
        else:
            return num1 / num2
    elif operator == '%':
        return num1 % num2
    else:
        return "Opérateur non valide."

# Exemples d'appels de la fonction calcule avec différents opérateurs et nombres
resultat_addition = calcule(10, '+', 5)
print("Résultat de l'addition :", resultat_addition)

resultat_multiplication = calcule(8, '*', 3)
print("Résultat de la multiplication :", resultat_multiplication)

resultat_division = calcule(15, '/', 0)
print("Résultat de la division :", resultat_division)

