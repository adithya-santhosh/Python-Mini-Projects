from turtle import Turtle
import random

COLORS = ["red", "blue", "green", "orange", "yellow", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

class CarManager:

    def __init__(self):
        self.all_car = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            y_coordinate = random.randint(-200, 210)
            new_car.goto(300, y_coordinate)
            self.all_car.append(new_car)

    def move_car(self):
        for cars in self.all_car:
            cars.setheading(180)
            cars.forward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT
