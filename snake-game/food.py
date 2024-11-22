from turtle import Turtle
import random

class Food(Turtle):  
    def __init__(self):
        super().__init__()
        self.shape("circle") # criando objeto Turtle dentro da classe filha food
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-240, 240)
        random_y = random.randint(-240, 240)
        self.goto(random_x, random_y) # permite que o objeto da classe food vá apareça em pontos aleatórios da coordenada (x,y)

