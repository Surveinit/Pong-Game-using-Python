from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 240)
        self.write(f"{self.l_score} - {self.r_score}", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.color("white")
        self.write(f"{self.l_score} - {self.r_score}", align=ALIGNMENT, font=FONT)

    def l_increase_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_increase_score(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
