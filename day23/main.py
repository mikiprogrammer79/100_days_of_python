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


game_alive = True
while game_alive:
    time.sleep(0.1)
    screen.update()




screen.exitonclick()