import time
from turtle import Turtle, Screen

# import Score class from scoreboard module
import scoreboard
from paddle import Paddle
from ball import Ball

# create an instance of the Score class
score = scoreboard.Score()

# initialize the screen
screen = Screen()
screen.tracer(0)

# set the screen background color and title, and set the screen size
screen.bgcolor("#1e1e1e")
screen.title("Pong")
screen.setup(width=800, height=600)

# create the right and left paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# set up the keyboard bindings for the left and right paddles
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

# listen for keyboard events
screen.listen()

# create the ball
ball = Ball()

# set the game_is_on flag to True
game_is_on = True

# main game loop
while game_is_on:
    # pause the game for a short period of time to slow down the ball's movement
    time.sleep(ball.move_speed)

    # update the screen
    screen.update()

    # move the ball
    ball.move()

    # Detects collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detects collision with right/left paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # Detects right misses
    if ball.xcor() > 380:
        # reset the ball's position
        ball.reset_position()

        # increase the left player's score and update the scoreboard
        score.l_increase_score()
        score.update_scoreboard()

    # Detects left misses
    if ball.xcor() < -380:
        # reset the ball's position
        ball.reset_position()

        # increase the right player's score and update the scoreboard
        score.r_increase_score()
        score.update_scoreboard()

# exit the game when the screen is clicked
screen.exitonclick()
