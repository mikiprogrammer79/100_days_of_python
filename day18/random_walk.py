# Generate a random walk with turtle graphics

import turtle as t
import random 


turtle = t.Turtle()

colours = ["coral", "brown", "orange", "red", "blue", "yellow", "green", "purple"]

pen_width = 1

heading = [0, 90, 180, 270]
for i in range(33):
    random_length = random.randint(1, 100)
    random_colour = random.choice(colours)
    turtle.color(random_colour)
    turtle.pensize(pen_width)
    pen_width += 1
    turtle.forward(random_length)
    turtle.setheading(random.choice(heading))

# Call screen and exit on click

screen = t.Screen()

screen.exitonclick()