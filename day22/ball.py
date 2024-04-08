from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        

    def move_ball(self, slope, direction):
        x = self.xcor() + direction
        y = self.ycor() + slope
        # Move ball
        self.setposition(x, y)    
