from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.fillcolor("White")
        self.setposition(pos)

    def up(self):
        new_position = self.ycor() + 20
        self.goto(self.xcor(), new_position)

    def down(self):
        new_position = self.ycor() - 20
        self.goto(self.xcor(), new_position)