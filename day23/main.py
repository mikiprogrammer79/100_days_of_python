# The Turtle Crossing Game

import time
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Turtle Crossing Game")
screen.tracer(0)

game_alive = True
while game_alive:
    time.sleep(0.1)
    screen.update()
    