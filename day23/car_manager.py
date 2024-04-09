from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "coral"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        random_color = random.randint(0, (len(COLORS) - 1))
        random_y = random.randint(-160, 170)
        self.shape("square")
        self.color(COLORS[random_color])
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.setposition(300, random_y)

        
    def move(self, level):  
        self.backward(STARTING_MOVE_DISTANCE + level * MOVE_INCREMENT)
        print(f"speed: {STARTING_MOVE_DISTANCE + level * MOVE_INCREMENT}")

