# import colorgram

# colors = colorgram.extract(r"C:\Users\55219\OneDrive\Documentos\100 days of code\18\image.jpg", 30)

# rgb_colors = []

# for color in colors: 
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r,g,b)
#    rgb_colors.append(new_color)
# print(rgb_colors)


# requisitos: 

# 10 x 10 filas de manchas
# pontos devem ter tamanho 20 e 50 passos de distância

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.penup() # evita traços enquanto a tartaruga se move

color_list = [(220, 149, 107), (140, 119, 8), (73, 127, 125), (14, 122, 175), (56, 10, 10), (78, 40, 65), (185, 90, 156), (56, 165, 55), (226, 152, 223), (119, 8, 14), (4, 86, 120), (251, 251, 0), (247, 247, 34), (227, 157, 227), (129, 3, 2), (120, 81, 107), (121, 122, 1), (12, 69, 93), (127, 172, 187), (132, 173, 148), (148, 143, 67), (214, 178, 176), (167, 209, 178), (161, 203, 215), (92, 141, 154), (165, 108, 106)]

num_dots = 10
dot_distance = 50
dot_size = 20
widht = (num_dots - 1) * dot_distance # largura
height = (num_dots - 1) * dot_distance # altura
x = -widht / 2 # posição horizontal (lado esquerdo da grade)
y = height / 2 # (topo da grade)

# posicionar turtle na posição inicial
for row in range(num_dots):
    tim.goto(x,(y - row * dot_distance))
    for dot in range(num_dots):
        random_rgb_color = random.choice(color_list) # uma nova cor é escolhida a cada iteração
        tim.dot(20, random_rgb_color)
        tim.forward(50)


screen = t.Screen()
screen.exitonclick()
