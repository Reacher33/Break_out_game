from turtle import Screen
from paddles import Paddle
from blocks import Blocks
from ball import Ball
from score import Scoreboard
import time


screen = Screen()
screen.bgcolor("Black")
screen.title("Breakout-Game")
screen.setup(width=800, height=600)
screen.tracer(0)


paddle = Paddle()
blocks = Blocks(rows=3, columns=10)
score = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

gaming = True
while gaming:
    time.sleep(0.1)
    ball.move()

    # Detect colling with wall
    if ball.ycor() > 280:
        ball.bounce_y()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.distance(paddle) < 63 and ball.ycor() < -240:
        ball.bounce_y()

    # Detect collision with block
    if blocks.is_collision(ball):
        score.point()

    # Detect when ball goes out of bound
    if ball.ycor() < -280:
        ball.reset_ball()

    screen.update()
screen.exitonclick()
