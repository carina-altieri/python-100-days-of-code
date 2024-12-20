from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
   
    def __init__(self):
        super().__init__() 
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def up(self): 
        new_ycor = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_ycor) # mantém o x atual e ajusta o y
        # ou: self.forward(MOVE_DISTANCE)
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else: 
            return False


        