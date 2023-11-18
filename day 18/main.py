from turtle import Turtle, Screen, colormode
import random as ra
may = Turtle()
screen = Screen()

colormode(255)


def make_shape(sides):
    may.color(ra.randint(0,255), ra.randint(0,255), ra.randint(0,255))
    for jkk in range(sides):
        may.forward(100)
        may.right(360/sides)


def random_color():
    r = ra.randint(0,255)
    g = ra.randint(0,255)
    b = ra.randint(0,255)
    colour = (r,g,b)
    return colour


def random_walk():
    num = [0, 90, 180, 270]
    may.color(random_color())
    may.forward(30)
    may.setheading(ra.choice(num))
# for i in range(3, 11):
#     make_shape(i)


def spirography(size_of_gap):
    for i in range(int(360/size_of_gap)):
        may.color(random_color())
        may.circle(100)
        may.setheading(may.heading() + size_of_gap)




may.speed(15)
# for i in range(200):
#     random_walk()

spirography(5)



screen.exitonclick()