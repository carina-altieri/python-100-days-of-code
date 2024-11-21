# snake game project
from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# 20x20 snake size

# criando objeto snake
snake = Snake() 

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update() # only update the screen when all the segments have moved forwards
    time.sleep(0.2)

    snake.move()


screen.exitonclick()
