

# Initialisation des variables
montant_investissement_initial = 10000  # Montant initial de l'investissement en euros
taux_rendement_annuel = 5  # Taux de rendement annuel en pourcentage

# Calcul du gain annuel en fonction du taux de rendement
gain_annuel = (montant_investissement_initial * taux_rendement_annuel) / 100
print(f"Le gain annuel avec un taux de rendement de {taux_rendement_annuel}% est de : {gain_annuel} euros")

# Augmentation du capital de l'investisseur de 5000 euros et augmentation du taux de rendement de 2%
montant_investissement_initial += 5000
taux_rendement_annuel += 2

# Calcul du nouveau gain de l'investisseur après l'augmentation et affichage du résultat
nouveau_gain_annuel = (montant_investissement_initial * taux_rendement_annuel) / 100
print(f"Avec un montant de {montant_investissement_initial} euros et un taux de rendement de {taux_rendement_annuel}%, le nouveau gain annuel est de : {nouveau_gain_annuel} euros")

# Retrait de 10% du montant total et diminution du taux de rendement de 1%
montant_investissement_initial -= 0.10 * montant_investissement_initial
taux_rendement_annuel -= 1

# Calcul du montant final de l'investissement après le retrait et affichage du nouveau gain
montant_final = (montant_investissement_initial * (100 + taux_rendement_annuel)) / 100
nouveau_gain_final = montant_final - montant_investissement_initial
print(f"Après le retrait de 10% du montant total, le nouveau montant final de l'investissement est de : {montant_final} euros")
print(f"Le nouveau gain après le retrait est de : {nouveau_gain_final} euros")


