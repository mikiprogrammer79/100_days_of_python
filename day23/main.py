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
score = Scoreboard()
game_over = Scoreboard()

# Screen event listeners
screen.listen()
screen.onkey(fun=player.move, key="Up")

traffic = []
green_light = 6

level = 0
game_alive = True
while game_alive:
    time.sleep(0.1)
    screen.update()
    score.show_score(level + 1)
    if green_light == 6: 
        car = CarManager()
        traffic.append(car)
        green_light = 0
    green_light += 1
    for obj in traffic:
        if player.ycor() >= 200:
            player.finish_line()
            level += 1
        obj.move(level)

        # Detect collision with cars
        if obj.distance(player) < 20:
            game_over.game_over()
            game_alive = False 

screen.exitonclick()