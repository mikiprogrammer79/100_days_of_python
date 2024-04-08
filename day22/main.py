# The Pong Game

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


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

# Create score
score = Score()


    # Event Listeners
screen.listen()

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")


slope = 1
direction = 1
game_alive = True
while game_alive:
    screen.update()
    
    # Detect Collision with wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        slope *= -1

    # Detect collision with paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -330 :
        direction *= -1
    elif ball.distance(right_paddle) < 50 and ball.xcor() > 330:
        direction *= -1
    

    # Move ball    
    ball.move_ball(slope, direction)

    # Detect when paddle misses the ball
    if ball.xcor() > 370:
        time.sleep(1.5)
        ball.goto(0, 0)
        # Keep score
        score.l_point()
    elif  ball.xcor() < -370:
        time.sleep(1.5)
        ball.goto(0, 0)
        # Keep score
        score.r_point()



screen.exitonclick()