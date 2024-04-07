# Snake Game

from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food


# Screen setup

screen = Screen()

screen.setup(width=600, height=600) # Screen size

screen.bgcolor("black") # Screen background color

screen.title("The Python Game") # Screen Title

screen.tracer(0) # turn off the tracer to help animation (show when update)


# Snake 

snake = Snake() # Create snake body
food = Food()

# Start screen event listeners

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_alive = True

while game_alive:
    
    screen.update() # Update screen 

    time.sleep(0.1) # Sleep for 1 second to avoid flashing (snake speed)

    snake.move_forward()    # Move snake
    
    # Detect collision with food using Turtle.distance(instance)
    if snake.head.distance(food) < 15:
        food.show_food()


        


# Move snake: Animating the snake segments









screen.exitonclick() # Exit screen on click

