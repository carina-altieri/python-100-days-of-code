from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self): # movendo-se para cima e para a direita
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.xcor() + self.y_move
        self.goto(new_xcor, new_ycor)

    def bounce_y(self):
        self.y_move *= -1 # para quicar, ao atingir determinada posição, é preciso fazer a bola ir para o sentido oposto
        self.move_speed *= 0.9
        
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()