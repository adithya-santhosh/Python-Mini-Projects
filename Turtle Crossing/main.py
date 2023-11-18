import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scorecard import ScoreCard

# SCREEN
screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()


# PLAYER
player = Player()

# CAR MANAGER
traffic = CarManager()

# SCORECARD
score = ScoreCard()

# VARIABLES
game_on = True
screen.onkey(player.move_forward, "Up")

while game_on:
    screen.update()
    time.sleep(0.09)
    traffic.create_car()
    traffic.move_car()

    # Detect collision with cars
    for car in traffic.all_car:
        if player.distance(car) < 21:
            game_on = False
            score.game_over()

    # Detect if the player Crossed the Door

    if player.successfully_crossed():
        player.go_to_start()
        traffic.level_up()
        score.update_level()

screen.exitonclick()