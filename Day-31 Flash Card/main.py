from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"



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
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

# Button
correct_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
correct_button = Button(image=correct_image, highlightthickness=0)
wrong_button = Button(image=wrong_image, highlightthickness=0)

correct_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)

window.mainloop()