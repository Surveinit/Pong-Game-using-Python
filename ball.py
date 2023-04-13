from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.bx = 10  # ball moving in
        self.by = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.bx, self.ycor() + self.by)
        # print(self.xcor(), self.ycor())

    def bounce_x(self):
        self.bx *= -1
        self.move_speed *= 0.9
        # print(self.bounce_y)

    def bounce_y(self):
        self.by *= -1
        self.move_speed *= 0.9
        # print(self.bounce_y)

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
