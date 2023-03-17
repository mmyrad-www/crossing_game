FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 1

        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def score_point(self):
        self.score += 1
        self.update_score()

    def game_finished(self):
        self.hideturtle()
        self.home()
        self.write("Game Over!",align="center",font=FONT)
