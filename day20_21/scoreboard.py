from turtle import Screen


class Scoreboard(Screen):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.show_score()

    def show_score(self):
        self.title(f"Score: {self.score}")
        self.score += 1

    