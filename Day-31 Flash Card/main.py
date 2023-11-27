from tkinter import *
import pandas
from random import randint
BACKGROUND_COLOR = "#B1DDC6"

# Pandas operation
french_pd = pandas.read_csv("data/french_words.csv")
new_data = french_pd.to_dict(orient="records")
def next_word():
    num = randint(0,100)
    new_word = new_data[num]["French"]
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=new_word)

# UserInterface
window = Tk()
window.title("Flash Card")
window.minsize()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Adding main bg image
canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0 )
card_back_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_back_image)
canvas.grid(row=0, column=0, columnspan=2)


# Canvas  create Text
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

# Button
correct_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
correct_button = Button(image=correct_image, highlightthickness=0, command=next_word)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_word)

correct_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)

window.mainloop()