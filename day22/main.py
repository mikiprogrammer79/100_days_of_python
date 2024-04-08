# The Pong Game

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball


# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black") # Background color
screen.title("The Pong Game") # Creen window title
screen.tracer(0) # Turn off animation


# Create a move a paddle right_paddle and left_paddle
right_paddle = Paddle(350)
left_paddle = Paddle(-350)

# Create the ball and make it move across the screen
ball = Ball()
    # Event Listeners
screen.listen()

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")


game_alive = True
while game_alive:
    screen.update()
    

# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when paddle misses the ball
# Keep score


screen.exitonclick()