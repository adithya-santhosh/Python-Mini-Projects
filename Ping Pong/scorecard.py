from turtle import Turtle


class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score()


    def write_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    def update_score(self,num):
        if num == 1:
            self.l_score += 1
            self.write_score()
        elif num == 0:
            self.r_score += 1
            self.write_score()
