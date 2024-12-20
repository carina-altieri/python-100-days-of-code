import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.up, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # detectando colisão com carros
    for car in car_manager.all_cars:
        if car.distance(player) < 20: # se o player estiver a menos de 20 pixels do centro do carro, significa que colidiu com o carro
            game_is_on = False
            scoreboard.game_over()

    # detectando quando o player chega ao outro lado
    if player.finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()