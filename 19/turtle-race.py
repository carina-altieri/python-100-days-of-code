from turtle import Turtle, Screen
import random

# turtle dimensions = 40x40
# 250 - (40/2) = 230
race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a color: ")
turtle_colors = ["red", "orange", "blue", "green", "yellow", "purple"]
y_position= [-80, -50, -20, 10, 40, 70]  
turtles = []

for turtle in range(6):
    t = Turtle(shape="turtle")
    t.color(turtle_colors[turtle])
    t.penup()
    t.goto(x=-230, y=y_position[turtle])
    turtles.append(t)
    
if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You won! The {winner_color} turtle is the winner!")
            else:
                print(f"You lost! The {winner_color} turtle is the winner!")
        distance = random.randint(0,10)
        turtle.forward(distance)

    

screen.exitonclick()