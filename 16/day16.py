# import turtle
# timmy = turtle.Turtle()

# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# métodos
# timmy.shape("turtle")
# timmy.color("coral")
#timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight) # objeto.atributo
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)