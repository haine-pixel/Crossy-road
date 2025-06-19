FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-215,255)
        self.current_stage = 1
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(f"Level: {self.current_stage}",move = False, align = "center", font = FONT)

    def update_scoreboard(self):
        self.current_stage += 1
        self.scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER",move = False, align = "center", font = FONT)

