# from turtle import Turtle, Screen
#
#
# krip = Turtle()
# print(krip)
# krip.shape("turtle")
# krip.color("chartreuse3")
# krip.circle(80)
# krip.forward(100)
# krip.right(50)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
#

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"
print(table)