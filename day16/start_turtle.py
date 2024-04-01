# First steps with the Turtle module

from turtle import Turtle, Screen

johny = Turtle()
tommy = Turtle()

johny.shape("turtle")
johny.color("yellow")
johny.forward(100)
johny.left(280)
johny.forward(100)

tommy.shape("turtle")
tommy.color("red")
tommy.forward(100)
tommy.left(100)
tommy.penup()
tommy.forward(100)


screen = Screen()
screen.exitonclick()
