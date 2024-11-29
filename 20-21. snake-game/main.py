# snake game project
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# 20x20 snake size

# criando objeto snake, objeto food e objeto score
snake = Snake() 
food = Food()
scoreboard = Scoreboard()

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

    # detectar colisão com comidas usando o método distance para comparar a distância entre a cabeça da snake (primeiro segmento) e food
    if snake.snake_head.distance(food) < 15: # 15 pixels, considerando que a dimensão de food é 10x10
        food.refresh()
        snake.snake_extend()
        scoreboard.increase_score()

    # detectar colisão com parede:
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
            scoreboard.reset()
            snake.reset()

    # detectar colisão com o prórpio rabo
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
