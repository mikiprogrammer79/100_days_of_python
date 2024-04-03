# Draw a Dashed Line with turtle

from turtle import Turtle, Screen

pencil = Turtle()

pencil.color("gray")

# Draw a dashed line

for i in range(10):
    pencil.forward(10)
    pencil.penup()
    pencil.forward(10)
    pencil.pendown()

# Call screen and exit on click
screen = Screen()
screen.exitonclick()
