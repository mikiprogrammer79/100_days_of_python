from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(-350, 0)