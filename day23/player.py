from turtle import Turtle


STARTING_POSITION = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200
UP = 90

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(UP)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def finish_line(self):
        self.goto(STARTING_POSITION)
