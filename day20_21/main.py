# Snake Game

from turtle import Turtle, Screen


screen = Screen()

screen.setup(width=600, height=600) # Screen size

screen.bgcolor("black") # Screen background color

screen.title("The Python Game") # Screen Title

screen.tracer(0) # turn off the tracer to help animation (show when update)


tail = [(0, 0), (-20, 0), (-40, 0)] # List of segments coor

snake_segments = []

# Create a snake body (3 squares 20x20px)

for x_y in tail:
    segment = Turtle(shape= "square")
    segment.penup()
    segment.color("white")
    segment.goto(x_y)
    snake_segments.append(segment)

# Move snake

game_alive = True

while game_alive:
    
    for seg in snake_segments:
        seg.forward(20)
        screen.update()


# Move snake: Animating the snake segments









screen.exitonclick() # Exit screen on click

