# Paddle
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1) # Strecting square to look like a rectangle LOL
        self.penup()
        self.goto(position)

    def move_up(self):
        y = self.ycor() + 40  # Get the current y-coordinate and add 40 units to move it up
        self.goto(self.xcor(), y)

    def move_down(self):
        y = self.ycor() - 40
        self.goto(self.xcor(), y)
