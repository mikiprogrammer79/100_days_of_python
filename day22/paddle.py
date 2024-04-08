from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(350, 0)

    def move_up(self):
        self.setheading(90)
        self.forward(20)

    def move_down(self):
        self.setheading(270)
        self.forward(20)