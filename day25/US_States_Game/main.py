from turtle import Turtle, Screen


screen = Screen()

screen.title("US States Game")
image = "day25/US_States_Game/blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()

turtle.shape(image)

def get_coordenates(x, y):
    print(x, y)

turtle.onclick(get_coordenates)
screen.mainloop()



# screen.exitonclick()
