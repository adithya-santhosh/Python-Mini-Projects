import turtle
import pandas
from mapping import Mapping
map_tur = Mapping()

screen = turtle.Screen()
screen.title("US States Game")
# image = "blank_states_img.gif"
image = "indian_states_img.gif"
screen.addshape(image)
screen.setup(1000,800)
turtle.shape(image)


#file = pandas.read_csv("50_states.csv")
file = pandas.read_csv("indian_states.csv")
states = file.state
st = states.to_list()
all_correct_guess = []
score = 0
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

#turtle.mainloop()
while len(all_correct_guess) < 50:

    answer_state = screen.textinput(title = f"{score}/50 Correct States ", prompt="What's another state name ")
    a = answer_state.title()
    if a == "Exit":
        missing_states = [each_states for each_states in st if each_states not in all_correct_guess]
        break
    if a in st:
        all_correct_guess.append(a)
        score += 1
        state_guessed = file[file.state == a]
        xcor = int(state_guessed.x.iloc[0])
        ycor = int(state_guessed.y.iloc[0])
        map_tur.write_on_map(xcor, ycor, a)

states_to_learn = pandas.DataFrame(missing_states)
states_to_learn.to_csv("States_Needed_To_Learn_indian.csv")
screen.exitonclick()






