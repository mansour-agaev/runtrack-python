
def est_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def type_triangle(a, b, c):
    if a == b == c:
        return "équilatéral"
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "rectangle et isocèle"
        else:
            return "isocèle"
    elif a != b != c:
        return "quelconque"

# Demander à l'utilisateur les longueurs des côtés du triangle
a = float(input("Entrez la longueur du côté a : "))
b = float(input("Entrez la longueur du côté b : "))
c = float(input("Entrez la longueur du côté c : "))

# Vérifier si les longueurs permettent de former un triangle
if est_triangle(a, b, c):
    print("Il est possible de construire un triangle avec ces longueurs.")
    print("Ce triangle est de type :", type_triangle(a, b, c))
else:
    print("Impossible de former un triangle avec ces longueurs.")




