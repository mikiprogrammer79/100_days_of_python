from turtle import Turtle

FONT = ("Courier", 24, "normal" )
SCORE_POSITION = (-250, 200)
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        
        
    def show_score(self, level):
        self.goto(SCORE_POSITION)
        self.clear()
        self.write(f"Level: {level}", font=FONT)

    def game_over(self):
        self.write(f"Game Over!!",align="center", font=FONT)
        

