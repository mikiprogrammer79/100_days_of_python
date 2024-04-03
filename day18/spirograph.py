# Draw a Spirograph using random colours

import turtle as t
import random

t.colormode(255)

turtle = t.Turtle()


def circle_with_random_color():
    """Make a circle with a RGB random colour"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.pencolor((r, g, b))
    turtle.circle(100)


# Set speed to fastest

turtle.speed("fastest")

# Draw a circles in a loop, while degree < 360

degree = turtle.heading()

while degree < 360:
    print(degree)
    circle_with_random_color()
    turtle.setheading(degree + 5)
    degree += 5
    

# Call screen and exit on click

screen = t.Screen()
screen.exitonclick()