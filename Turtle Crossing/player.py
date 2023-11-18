from turtle import Turtle
STARTING_POSITION = (0, -260)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 240


class Player (Turtle):

    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.shape("turtle")
        self.shapesize(1)
        self.go_to_start()

    def go_to_start(self):
        self.setposition(STARTING_POSITION)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def successfully_crossed(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False
