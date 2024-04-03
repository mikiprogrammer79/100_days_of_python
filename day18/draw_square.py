# Draw an square with Turtle

from turtle import Turtle, Screen

vinny = Turtle()

vinny.shape("turtle")

vinny.color("coral")

for i in range(4):
    vinny.forward(100)
    vinny.left(90)

# Call screen and exit on click

screen = Screen()

screen.exitonclick()