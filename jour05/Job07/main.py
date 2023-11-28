def arrondir_notes(liste_notes):
    notes_arrondies = []
    
    for note in liste_notes:
        if note >= 40:  # Vérifier si l'étudiant a réussi le test
            multiple_de_5_superieur = (note // 5) * 5 + 5  # Trouver le prochain multiple de 5 supérieur
            if multiple_de_5_superieur - note < 3:  # Vérifier s'il est à moins de 3 points du multiple de 5
                notes_arrondies.append(multiple_de_5_superieur)  # Arrondir à ce multiple de 5
            else:
                notes_arrondies.append(note)  # Garder la note telle quelle
        else:
            notes_arrondies.append(note)  # Garder la note telle quelle
    
    return notes_arrondies

# Exemple d'utilisation de la fonction avec une liste de notes
liste_notes_eleves = [65, 42, 78, 39, 91, 54]
notes_arrondies = arrondir_notes(liste_notes_eleves)
print(notes_arrondies)

        