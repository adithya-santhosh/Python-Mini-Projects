from tkinter import *

window = Tk()
window.title("Miles Converter")
window.config(pady=10, padx=10)


def calculate():
    km = float(entry_input.get())
    miles = int(km * 1.6)
    lb_4.config(text=miles)


# Label
lb_1 = Label(text="Km")
lb_1.grid(row=0, column=2)

lb_2 = Label(text="is equal to ")
lb_2.grid(row=1, column=0)

lb_3 = Label(text="Miles")
lb_3.grid(row=1, column=2)

lb_4 = Label(text="0")
lb_4.grid(row=1, column=1)
# Entry
entry_input = Entry(width=5)
entry_input.grid(row=0, column=1)

# Button
button=Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)
window.mainloop()