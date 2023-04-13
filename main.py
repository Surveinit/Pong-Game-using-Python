import time
from turtle import Turtle, Screen

import scoreboard
from paddle import Paddle
from ball import Ball
from scoreboard import *

score = scoreboard.Score()

screen = Screen()
screen.tracer(0)

screen.bgcolor("#1e1e1e")
screen.title("Pong")
screen.setup(width=800, height=600)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.listen()
ball = Ball()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detects collision with up and down
    if ball.ycor() > 280 or ball.ycor() < -280:
        # print("Collision detected!")
        ball.bounce_y()

    # Detects collision with right/left paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # Detects r misses
    if ball.xcor() > 380:
        # print("R lose")
        ball.reset_position()
        score.l_increase_score()
        score.update_scoreboard()

    # Detects l misses
    if ball.xcor() < -380:
        # print("L lose")
        ball.reset_position()
        score.r_increase_score()
        score.update_scoreboard()

screen.exitonclick()

# TODO: Increase the speed of the ball after hitting the paddle
