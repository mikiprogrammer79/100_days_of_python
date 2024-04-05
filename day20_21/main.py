# Snake Game

from turtle import Turtle, Screen
import time

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
    
    screen.update() # Update screen 

    time.sleep(0.1) # Sleep for 1 second to avoid flashing

    for index in range(len(snake_segments) - 1, 0, -1): # (start=3, stop=0, step=-1)
        new_x = snake_segments[index - 1].xcor()
        new_y = snake_segments[index -1].ycor()
        snake_segments[index].goto(new_x, new_y)
        print(f"{new_x, new_y}")
    
    snake_segments[0].forward(20)
        


# Move snake: Animating the snake segments









screen.exitonclick() # Exit screen on click

