# The Turtle Crossing Game

import time
from turtle import Turtle, Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Turtle Crossing Game")
screen.tracer(0)


player = Player()


# Screen event listeners
screen.listen()
screen.onkey(fun=player.move, key="Up")

traffic = []
green_light = 6

game_alive = True
while game_alive:
    time.sleep(0.1)
    screen.update()
    if green_light == 6: 
        car = CarManager()
        traffic.append(car)
        green_light = 0
    green_light += 1
    for obj in traffic:
        obj.move()

    if player.ycor() >= 200:
        player.finish_line()
        for obj in traffic:
            obj.level_up()
            

screen.exitonclick()