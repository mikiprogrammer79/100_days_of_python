from turtle import Turtle, Screen
import pandas


screen = Screen()

screen.title("US States Game")
image = "day25/US_States_Game/blank_states_img.gif"
screen.addshape(image)


turtle = Turtle()

turtle.shape(image)

df = pandas.read_csv("day25/US_States_Game/50_states.csv")

states = df["state"].to_list()

records = []
points = 0
game_alive = True
while game_alive:
    user_input = screen.textinput(f"{points}/50 Guess the US States", "Type a US State: ")
    records.append(user_input.title())
    if user_input.lower() == "exit":
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
        if user_input.title() not in records[:-1]:
            points += 1
    else:
        pass


# Get coordenates on screen click
# def get_coordenates(x, y):
    # print(x, y)

# turtle.onclick(get_coordenates)
# screen.mainloop()
