from tkinter import *


def button_clicked():
    user_text=input_val.get()
    print("I got Clicked!!!")
    my_label.config(text=user_text)


window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=400)
window.config(padx=100,pady=100)

# Label
my_label = Label(text="I Am A Label ", font=("Arial", 18))
# my_label["text"] = "New Text"
my_label.config(text="Text")
my_label.grid(column=0, row=0)

# Button
button = Button(text='Click Me', command=button_clicked)
button.grid(column=1, row=1)

button1 = Button(text='New Button',command=button_clicked)
button1.grid(column=2, row=0)

# Entry
input_val = Entry()
input_val.grid(column=3, row=3)


window.mainloop()
