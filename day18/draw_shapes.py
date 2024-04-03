# Draw different shapes: Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon, Nonagon, Decagon
# Angle = 360 / sizes 

from turtle import Turtle, Screen

pen = Turtle()

colours = {
    "triangle": ["red", 120, 3],
    "square": ["coral", 90, 4], 
    "pentagon": ["purple", 72, 5],
    "hexagon": ["green", 60, 6],
    "heptagon": ["blue", (360/7), 7],
    "octagon": ["orange", 45, 8],
    "nonagon": ["yellow", 40, 9],
    "decagon": ["brown", 36, 10],
    }

# Draw shapes

for key in colours:
    pen.color(colours[key][0])    
    for i in range(colours[key][2]):
        pen.right(colours[key][1])
        pen.forward(100)


# Call screen and exit on click

screen = Screen()
screen.exitonclick()
