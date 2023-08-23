from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detects collision with walls
    if ball.ycor() >= 270.00 or ball.ycor() <= -270.00:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 55 and ball.xcor() > 320 or ball.distance(l_paddle) < 55 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when Right paddle misses
    if ball.xcor() > 420:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when Left paddle misses
    elif ball.xcor() < -420:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
