from turtle import Turtle
from players import Players


class Scoreboard(Turtle, Players):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.player_names = Players()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 270)
        self.write(f"{self.player_names.player_1}: {self.l_score}", align="center", font=("Courier", 18, "normal"))
        self.goto(100, 270)
        self.write(f"{self.player_names.player_2}: {self.r_score}", align="center", font=("Courier", 18, "normal"))
        self.goto(0, 240)
        self.write(f"Enter 'q' to end the game", align="center", font=("Courier", 13, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def winner(self):
        if self.l_score > self.r_score:
            self.goto(0, 0)
            self.write(f"{self.player_names.player_1} is the winner", align="center", font=("Courier", 20, "normal"))
        if self.l_score < self.r_score:
            self.goto(0, 0)
            self.write(f"{self.player_names.player_2} is the winner", align="center", font=("Courier", 20, "normal"))
        if self.l_score == self.r_score:
            self.goto(0, 0)
            self.write(f"Draw!!", align="center", font=("Courier", 20, "normal"))