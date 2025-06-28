import tkinter as tk

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    if timer:
        reps = 0
        timer_label.config(text="Timer", fg=GREEN)
        canvas.itemconfig(timer_text, text="00:00")
        checkmarks.config(text="")
        window.after_cancel(timer)  # Cancel the timer if it's running

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_button_function(): 
    global reps
    reps += 1

    work_sessions = WORK_MIN * 60
    short_break_sessions = SHORT_BREAK_MIN * 60
    long_break_sessions = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # Long Break
        timer_label.config(text="Long Break", fg=RED)
        start_timer(long_break_sessions)
    elif reps % 2 == 0:
        # Short Break
        timer_label.config(text="Short Break", fg=PINK)
        start_timer(short_break_sessions)
    else: 
        # Work Session
        timer_label.config(text="Work", fg=GREEN)
        start_timer(work_sessions)

    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_timer(count):
    global timer
    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        timer = window.after(1000, start_timer, count-1)
    else:
        start_button_function()
        # Update checkmarks
        marks = "✔" * (reps // 2)
        checkmarks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)
window.minsize(width=700, height=400)
# Configure grid to center everything
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)


#Tomato Image
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="pomodoro_app\image.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text =canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Timer
timer_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

#start butto
start_button = tk.Button(text="Start", command=start_button_function, bg=GREEN, fg="white", font=(FONT_NAME, 12, "bold"), highlightthickness=0)
start_button.grid(column=0, row=2)

#reset button
reset_button = tk.Button(text="Reset", command=reset_timer, bg=RED, fg="white", font=(FONT_NAME, 12, "bold"), highlightthickness=0)
reset_button.grid(column=2, row=2)

#Checkmark
checkmarks = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
checkmarks.grid(column=1, row=3)







window.mainloop()