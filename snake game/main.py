from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import ScoreCard

scorecard = ScoreCard()
new_food = Food()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    if snake.head.distance(new_food) < 15:
        new_food.new_location()
        snake.extend()
        scorecard.increase_scorecard()

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scorecard.reset_game()
        snake.reset()

    for segment in snake.snake_segment[1:]:
        if snake.head.distance(segment) < 8:
            scorecard.reset_game()
            snake.reset()

screen.exitonclick()
