from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.show_score()
        self.hideturtle()
        

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT )
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGMENT, font=FONT)
