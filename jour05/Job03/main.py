
def draw_triangle(height):
    for i in range(height):
        if i == height - 1:
            print('_' * (2 * height - 1))  # Base du triangle
        else:
            spaces = ' ' * (height - i - 1)
            if i == 0:
                print(spaces + '/')
            else:
                print(spaces + '/' + ' ' * (2 * i - 1) + '\\')

# Appel de la fonction avec la hauteur = 5
draw_triangle(5)




