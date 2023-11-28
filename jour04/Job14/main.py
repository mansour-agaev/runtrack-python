def my_long_word(n, texte):
    mots = ""
    mot = ""
    for caractere in texte:
        if caractere != " ":
            mot += caractere
        else:
            if len(mot) > n:
                mots += mot + " "
            mot = ""
    # Vérifier le dernier mot dans la phrase
    if len(mot) > n:
        mots += mot
    return mots

# Exemple d'utilisation
resultat = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")

# Afficher le résultat
print("Output :", resultat)



