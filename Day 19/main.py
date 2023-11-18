from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
colour = ["red", "blue", "yellow", "green", "orange", "violet"]
y_position = [80, 55, 30, 5, -20, -45]
screen.setup(height=400, width=600)
user_input = screen.textinput(title="Make you're Bet", prompt="Which turtle will will the race? Enter the color:-")
all_turtle = []


for turtle_index in range(6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colour[turtle_index])
    t.goto(x=-280, y=y_position[turtle_index])
    all_turtle.append(t)


if user_input :
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 280:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've Won. The {winning_color} turtle is the winner")
            else:
                print(f"You've Lose. The {winning_color} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




screen.exitonclick()