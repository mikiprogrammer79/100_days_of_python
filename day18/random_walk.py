# Generate a random walk with turtle graphics

import turtle as t
import random 


turtle = t.Turtle()

colours = ["coral", "brown", "orange", "red", "blue", "yellow", "green", "purple"]

pen_width = 1

for i in range(33):
    random_length = random.randint(1, 100)
    random_index = random.randint(0, (len(colours) - 1))
    random_degree = random.randint(0, 360)
    turtle.color(colours[random_index])
    turtle.pensize(pen_width)
    pen_width += 1
    turtle.forward(random_length)
    turtle.right(random_degree)
    turtle.backward(random_length)
    turtle.right(45)

# Call screen and exit on click

screen = t.Screen()

screen.exitonclick()