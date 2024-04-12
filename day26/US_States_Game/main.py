from turtle import Turtle, Screen
import pandas


screen = Screen()

screen.title("US States Game")
image = "day26/US_States_Game/blank_states_img.gif"
screen.addshape(image)


turtle = Turtle()

turtle.shape(image)

df = pandas.read_csv("day26/US_States_Game/50_states.csv")

states = df["state"].to_list()

records = []
points = 0
game_alive = True
while game_alive:
    user_input = screen.textinput(f"{points}/50 Guess the US States", "Type a US State: ")
    records.append(user_input.title())
    if user_input.lower() == "exit":
        missing_states = [st for st in states if st not in records ]
        break
    if user_input.title() in states:
        answer = Turtle()
        answer.hideturtle()
        answer.penup()
        row = df[df.state == f"{user_input.title()}"]
        xcor = float(row.x)
        ycor = float(row.y)
        answer.goto(xcor, ycor)
        answer.write(f"{user_input.title()}")
        points += 1

# Create a csv file with the missing states
new_df = pandas.DataFrame(missing_states)

new_df.to_csv("day26/US_States_Game/missing_states.csv")
