# Turtle Race
# Choose a colour and make your bet.

from turtle import Turtle, Screen

import random


screen = Screen()


def create_turtle(name, color, start_y):
    """Create a turtle object and take it to start line""" 
    name = Turtle()
    name.penup()
    name.shape("turtle")
    name.color(color)
    name.goto(-230, start_y)
    all_turtles.append(name)

def move_forwards(name):
    random_steps = random.randint(1, 10)
    name.forward(random_steps)

def check_finish_line(name):
    global race_on
    finish_line_x = 230
    current_position_x = name.xcor()
    if finish_line_x < current_position_x:
        race_on = False
        winner.append(name.pencolor())


# Setup Screen size

screen.setup(width=500, height=400)

# Prompt the user to make his bet

user_input = screen.textinput("Make your bet", "“Which turtle will win the race? " +
                              "Choose color (red, yellow, green, blue, purple, orange): ")

colours = ["red", "yellow", "green", "blue", "purple", "orange"]

names = ["ferrari", "renault", "sauber", "red_bull", "mercedes", "mclaren"]

all_turtles = []

coor_y = 160

poll_position = False
race_on = False

if user_input in colours:
    poll_position = True


while poll_position:
    # Position turtles at the starting line
    for i in range(6):
        create_turtle(names[i], colours[i], coor_y)
        coor_y -= 60
    poll_position = False
    race_on = True

    winner = []

    while race_on:
        
        # Move turtles forwards with random steps and stop race when turtle get finish line (500, coor_y)
        for turtle in all_turtles:
            move_forwards(turtle)
            check_finish_line(turtle)
    
        if race_on:
            pass
        else:
            if winner[-1] == user_input:
                index = colours.index(winner[-1])
                print(f"The winner is the {winner[-1]} {names[index]} turtle. You win!")
            else:
                index = colours.index(winner[-1])
                print(f"Sorry, you have lost. The winner is the {winner[-1]} {names[index]} turtle")

            another_race = screen.textinput("Try another race", "Type 'y' for another race, or click screen for exit: ")

            if another_race.lower() == "y":
                new_coor_y = 160
                for turtle in all_turtles:
                    turtle.goto(-230, new_coor_y)
                    new_coor_y -= 60
                race_on = True
                
# Exit screen on click

screen.exitonclick()