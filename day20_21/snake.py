from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
STEP_FORWARD = 20

class Snake:

    def __init__(self):
        self.snake_objects = []    
        self.create_body()
        self.head = self.snake_objects[0]

    def create_body(self):
        for position in START_POSITION:
            snake = Turtle(shape="square")
            snake.penup()
            snake.color("White")
            snake.goto(position)
            self.snake_objects.append(snake)
        

    def move_forward(self):
        for index in range(len(self.snake_objects) - 1, 0, -1): # (start=3, stop=0, step=-1)
            new_x = self.snake_objects[index - 1].xcor()
            new_y = self.snake_objects[index -1].ycor()
            self.snake_objects[index].goto(new_x, new_y)

        self.head.forward(STEP_FORWARD)        

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)