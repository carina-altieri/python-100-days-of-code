from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")

screen.tracer(0) # controla a exibição da tela - 0 desliga a animação
# screen.tracer(True) - atualiza a tela após configurada a posição oficial da raquete, assim, a tela só é exibida quando todos os itens já tiverem sido configurados

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

   # detectar colisão com parede (topo e parte inferior)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detectar colisão com as raquetes
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detectar quando a raquete perde a bola
    # raquete direita
    if  ball.xcor() > 380:
        ball.reset_position() 
        scoreboard.left_point()
    
    # raquete esquerda
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()
        
screen.exitonclick()