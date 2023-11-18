from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorecard import Scorecard
import time

# SCREEN ITEMS
screen = Screen()
screen.tracer(0)
screen.title("Ping Pong")
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.listen()


# VARIABLES
game_on = True

# PADDLE ITEMS
l_paddle = Paddle((-383, 0))
r_paddle = Paddle((380, 0))
screen.onkey(l_paddle.up, key="w")
screen.onkey(l_paddle.down, key="s")
screen.onkey(r_paddle.up, key="Up")
screen.onkey(r_paddle.down, key="Down")

# BALL ITEMS
ball = Ball()
# SCORECARD
score = Scorecard()

while game_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # COLLISION DETECT
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # DETECT COLLISION WITH PADDLE
    if ball.xcor() >= 360 and ball.distance(r_paddle) < 50 or ball.xcor() <= -360 and ball.distance(l_paddle) < 50:
        ball.deflect()

    # IF BALL WENT OUT
    if ball.xcor() > 390:
        ball.restart()
        score.update_score(1)
    elif ball.xcor() < -390:
        ball.restart()
        score.update_score(0)


screen.exitonclick()
