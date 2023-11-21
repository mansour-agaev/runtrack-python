

# Définition des variables représentant le produit
nom_produit = "Ordinateur portable"
prix_unitaire = 1200.00
quantite_stock = 50

# Affichage des informations du produit
print("Informations du produit :")
print(f"Nom du produit : {nom_produit}")
print(f"Prix unitaire : {prix_unitaire} €")
print(f"Quantité en stock : {quantite_stock}")

# Ajout de produits en stock
quantite_achetee = int(input("Entrez la quantité de produits que vous souhaitez acheter : "))
quantite_stock += quantite_achetee

# Mise à jour du prix unitaire suite à l'inflation de 10%
prix_unitaire *= 1.1

# Affichage des nouvelles informations sur le produit après l'ajout et l'inflation
print("\nInformations mises à jour du produit :")
print(f"Nom du produit : {nom_produit}")
print(f"Prix unitaire après inflation : {prix_unitaire} €")
print(f"Nouvelle quantité en stock : {quantite_stock}")

