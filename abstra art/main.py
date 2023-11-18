from turtle import Turtle, Screen, colormode
import random as rd
import colorgram as col
colour = col.extract("damien-hirst-severed-spots.jpg",10)


colormode(255)
t = Turtle()
t.shape("circle")
t.speed("fastest")
t.hideturtle()
t.penup()
t.setheading(225)
t.forward(300)
t.setheading(0)

for row in range(10):
    for col in range(10):
        current_colour = colour[rd.randint(0, 9)].rgb
        t.dot(20,current_colour)
        t.forward(50)
    t.back(500)
    t.left(90)
    t.forward(50)
    t.right(90)


screen = Screen()
screen.exitonclick()
