

def chiffrement_cesar(message, decalage):
    message_chiffre = ""
    for lettre in message:
        if lettre.isalpha():  # Vérifier si le caractère est une lettre
            # Obtenir la valeur ASCII de la lettre
            ascii_value = ord(lettre)
            # Gérer les majuscules
            if lettre.isupper():
                ascii_value = ((ascii_value - 65 + decalage) % 26) + 65
            # Gérer les minuscules
            else:
                ascii_value = ((ascii_value - 97 + decalage) % 26) + 97
            # Convertir la valeur ASCII décalée en lettre et l'ajouter au message chiffré
            lettre_chiffree = chr(ascii_value)
            message_chiffre += lettre_chiffree
        else:
            # Si le caractère n'est pas une lettre, l'ajouter tel quel au message chiffré
            message_chiffre += lettre
    return message_chiffre

# Exemple d'utilisation
message_original = "Bonjour, comment allez-vous ?"
decalage = 3

# Chiffrer le message avec un décalage de 3
message_chiffre = chiffrement_cesar(message_original, decalage)

# Afficher le message chiffré
print("Message chiffré :", message_chiffre)
