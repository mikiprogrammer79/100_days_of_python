from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.show_score()
        self.hideturtle()
        

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score} / High Score: {self.high_score}", align=ALIGMENT, font=FONT )
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGMENT, font=FONT)
