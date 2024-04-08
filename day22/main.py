# The Pong Game

from turtle import Turtle, Screen
from paddle import Paddle


# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black") # Background color
screen.title("The Pong Game") # Creen window title


# Create a move a paddle
right_paddle = Paddle()

    # Event Listeners
screen.listen()

screen.onkey(left_paddle.move_up, "Up")
screen.onkey(left_paddle.move_down, "Down")



# Create another paddle
# Create the ball and make it move across the screen
# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when paddle misses the ball
# Keep score


screen.exitonclick()