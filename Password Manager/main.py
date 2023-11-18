from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    search_website = entry_web.get()
    try:
        with open("My_Passwords.json", "r") as ps:
            details = json.load(ps)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="THE following file is Empty")
    else:
        if search_website in details:
            messagebox.showinfo(title="Information", message=f"Email={details[search_website]['email']}"
                                                           f"\nPassword={details[search_website]['password']}")
        else:
            messagebox.showinfo(title="error", message=f"No details for {search_website} exists.")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def enter_record():

    new_email = entry_email.get()
    new_website = entry_web.get()
    new_password = entry_password.get()
    new_data = {
        new_website: {
            "email": new_email,
            "password": new_password
        }
    }
    if len(new_password) == 0 or len(new_website) == 0:
        messagebox.showerror(title="Warning", message="You have left an empty field.")
    else:
        try:
            with open("My_Passwords.json", "r") as ps:
                data = json.load(ps)

        except FileNotFoundError:
            with open("My_Passwords.json", "w") as ps:
                json.dump(new_data, ps, indent=4)

        else:
            data.update(new_data)

            with open("My_Passwords.json", "w") as ps:
                json.dump(data, ps, indent=4)
        finally:
            entry_web.delete(0, END)
            entry_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, columnspan=1)


# Website
label_web = Label(text="Website :", font=(FONT_NAME, 10), pady=10)
entry_web = Entry(width=36)
entry_web.focus()
label_web.grid(row=1, column=0)
entry_web.grid(row=1, column=1)
# Email
label_email = Label(text="Email/Username :", font=(FONT_NAME, 10))
entry_email = Entry(width=36)
entry_email.insert(0,"adithyasanthosh4@gmail.com")
label_email.grid(row=2, column=0,columnspan=1)
entry_email.grid(row=2, column=1, columnspan=2)
# Password
label_password = Label(text="Password :",font=(FONT_NAME, 10), pady=10)
entry_password = Entry(width=35)
password_button = Button(text="Generate", command=create_password)
label_password.grid(row=3, column=0)
entry_password.grid(row=3, column=1, columnspan=1)
password_button.grid(row=3, column=2)
# Submit Button
submit_button = Button(text="Add", width=36, command=enter_record, pady=10)
submit_button.grid(row=4, column=1, columnspan=3)
# Search
search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2, columnspan=1)


window.mainloop()