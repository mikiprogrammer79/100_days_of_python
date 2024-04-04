# Etch a Sketch with turtle graphics using event listeners
# W: Forwards; S: Backwards; A: Counter-Clockwise; D: Clockwise
# C: Clear the screen

from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

screen.listen()


def move_forward():
    t.forward(10)

def move_backward():    
    t.backward(10)

def counter_clockwise():
    t.left(10)

def clockwise():
    t.right(10)

def clear():
    t.clear()
    t.penup()
    t.setposition(0, 0)
    t.setheading(0)

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

# Exit screen on click

screen.exitonclick()