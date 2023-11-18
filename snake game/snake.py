from turtle import Turtle
import time
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270


class Snake:
    def __init__(self):
        self.snake_segment = []
        self.create_snake()
        self.head = self.snake_segment[0]

    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_segment(position=i)

    def add_segment(self,position):
        sq_turtle = Turtle(shape="square")
        sq_turtle.penup()
        sq_turtle.color("white")
        sq_turtle.goto(position)
        self.snake_segment.append(sq_turtle)

    def extend(self):
        self.add_segment(self.snake_segment[-1].position())

    def reset(self):
        for seg in self.snake_segment:
            seg.goto(1000,1000)
        self.snake_segment.clear()
        self.create_snake()
        self.head = self.snake_segment[0]
    def move(self):
        for seg in range(len(self.snake_segment) - 1, 0, -1):
            last_segment = self.snake_segment[seg]
            move_to_segment = self.snake_segment[seg - 1]
            last_segment.goto(move_to_segment.pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
