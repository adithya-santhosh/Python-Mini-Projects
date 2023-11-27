from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
# For German
german_pd = pandas.read_csv("data/german_words.csv")
german_dict = german_pd.to_dict(orient="records")


def german_word():
    german_word = choice(german_dict)
    canvas.itemconfig(title, text="German")
    canvas.itemconfig(word, text=german_word["German"])


# Pandas operation for french
french_pd = pandas.read_csv("data/french_words.csv")
new_data = french_pd.to_dict(orient="records")


def next_word():
    global current_card, timer
    window.after_cancel(timer)
    canvas.itemconfig(canvas_image, image=card_front_image)
    current_card = choice(new_data)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    timer = window.after(3000, func=flip_card)



# Flash Card
def flip_card():
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_image,)
    canvas.itemconfig(title, text="English", fill="white")


# UserInterface
window = Tk()
window.title("Flash Card")
window.minsize()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=flip_card)

# Adding main bg image
canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0 )
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)


# Canvas  create Text
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Button
correct_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
correct_button = Button(image=correct_image, highlightthickness=0, command=next_word)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_word)

correct_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)

next_word()
window.mainloop()