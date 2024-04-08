# The Pong Game

from turtle import Turtle, Screen
from paddle import Paddle


# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black") # Background color
screen.title("The Pong Game") # Creen window title
screen.tracer(0) # Turn off animation


# Create a move a paddle right_paddle and left_paddle
right_paddle = Paddle(350)
left_paddle = Paddle(-350)

    # Event Listeners
screen.listen()

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

game_alive = True
while game_alive:
    screen.update()

# Create the ball and make it move across the screen
# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when paddle misses the ball
# Keep score


screen.exitonclick()