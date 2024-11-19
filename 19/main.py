from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards(): # função que será ativada quando uma chave for chamada. ex: espaço
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()