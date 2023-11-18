from turtle import Turtle
FONT = ('Arial', 20, 'normal')


class ScoreCard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        with open("data.txt") as data_score:
            self.high_score = int(data_score.read())
        self.hideturtle()
        self.pencolor("white")
        self.current_score = 0
        self.write_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align="Center" , font=FONT)


    def update_score(self):
        self.clear()
        self.write_score()

    def increase_scorecard(self):
        self.current_score += 1
        self.update_score()

    def write_score(self):
        self.goto(-150, 250)
        self.write(f"Score:{self.current_score}  HighScore: {self.high_score}", True,font=FONT)

    def reset_game(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w") as data_score:
                data_score.write(str(self.current_score))
        self.current_score = 0
        self.update_score()


