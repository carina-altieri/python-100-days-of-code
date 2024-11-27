from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__() 
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1) # todas as tartarugas começam com 20x20
        self.setposition(position)

    def up(self):
        new_ycor = self.ycor() + 20 # raquete move 20 px
        self.goto(self.xcor(), new_ycor)

    def down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)