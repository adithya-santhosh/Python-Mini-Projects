from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK_MARK = "✔"
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_1.config(text="Timer", fg=GREEN)
    reps = 0
    label_2.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def star_timer():
    global reps
    reps += 1
    working_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label_1.config(text="Long Break",fg=RED)
        count_down(long_break_min)
    elif reps % 2 == 0:
        label_1.config(text="Break",fg=PINK)
        count_down(short_break_min)
    else:
        label_1.config(text="Work",fg=GREEN)
        count_down(working_min)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps, timer
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        star_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += TICK_MARK
            label_2.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.minsize()
window.config(padx=50, pady=50, bg=YELLOW)


canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 105, image=tomato_img)
canvas.grid(row=1, column=1)

timer_text = canvas.create_text(105, 113, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))

# Label
label_1 = Label(text="TIMER", font=(FONT_NAME, 60), fg=GREEN, bg=YELLOW)
label_1.grid(row=0, column=1)
label_2 = Label(font=(FONT_NAME, 15), fg=GREEN, bg=YELLOW)
label_2.grid(row=3, column=1)

# Button
start_button = Button(text="Start", font=(FONT_NAME, 10), command=star_timer)
reset_button = Button(text="Reset", font=(FONT_NAME, 10), command=reset_timer)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)

window.mainloop()
