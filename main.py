from tkinter import *
import math

reps = 0
reset_timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_time():
    start["state"] = "active"
    window.after_cancel(reset_timer)
    label.config(text="Timer")
    canvas.itemconfig(timer, text="00:00")
    check.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    start["state"] = "disabled"
    if reps % 8 == 0:
        count_down(20 * 60)
        label.config(text="Long Break", fg="red")
    elif reps % 2 != 0:
        count_down(25 * 60)
        label.config(text="Study Time", fg="green")
    else:
        count_down(5 * 60)
        label.config(text="Short Break", fg="blue")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global reset_timer
        reset_timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔️"
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=80, pady=40, bg="pink")

canvas = Canvas(width=200, height=224, bg="pink", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(100, 130, text="00:00", font=("Courier", 36, "bold"))
canvas.grid(row=2, column=2)

label = Label()
label.config(text="Timer", font=("Courier", 30, "normal"), bg="pink", fg="red")
label.grid(row=1, column=2)

check = Label()
check.config(bg="pink", font=("Courier", 15, "normal"), pady=20)
check.grid(row=3, column=2)

start = Button()
start.config(text="Start", font=("Courier", 10, "normal"), fg="blue", command=start_timer)
start.grid(row=3, column=1)

reset = Button()
reset.config(text="Reset", font=("Courier", 10, "normal"), fg="blue", command=reset_time)
reset.grid(row=3, column=3)

window.mainloop()
