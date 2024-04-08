from turtle import Turtle

X_COR = 350

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(X_COR, 0)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(X_COR, new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(X_COR, new_y)