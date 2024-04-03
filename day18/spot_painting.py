# Create a Spot Painting like Hirst using random colours

import turtle as t
import colorgram
import random

spot = t.Turtle()

t.colormode(255)

colors = colorgram.extract('image.jpg', 6)


def random_color():
    """Generate a random color from the image.jpg color pallet"""
        
    random_color = colors[random.randint(0, (len(colors) - 1))]

    rgb = random_color.rgb 

    random_color = random.choice(colors)

    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]

    return (red, green, blue)


def row(number):
    """Take the arrow to the first column of the row and paint dots forward"""
    spot.setposition(-300, number)
    spot.dot(20, random_color())
    for i in range(20):
        spot.forward(30)
        spot.dot(20, random_color())
    spot.setposition(0, 0)

spot.penup()

spot.speed("fastest")


# Call row(number) function while number > -300

coord_y = 300

while coord_y > (-300): 
    
    row(coord_y)

    coord_y -= 30

# paint the bottom row
    
row(-300)

# Call screen and exit on click

screen = t.Screen()
screen.exitonclick()