from turtle import Turtle, Screen

# W = Forwards
# S = Backwards
# A = Counter-Clockwise 
# D = Clockwise
# E = Draw Curve
# C = Clear

t = Turtle()
screen = Screen()
t.speed(1)

def move_forwards():
    t.forward(50)

def move_backwards():
    t.forward(-50)

def move_counter_clockwise():
    t.left(10)

def move_clockwise():
    t.right(10)

def draw_curve_clockwise():
    t.circle(50, 180)

def draw_curve_count_clockwise():
    t.circle(-50, 180)

def clear_drawing():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="e", fun=draw_curve_clockwise)
screen.onkey(key="f", fun=draw_curve_count_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()