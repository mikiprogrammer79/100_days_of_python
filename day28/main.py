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
repetitions = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global repetitions
    repetitions += 1
    if repetitions == 1 or repetitions == 3 or repetitions == 5 or repetitions == 7:
        count_down(WORK_MIN * 60) 
        label.config(text="Work", fg=GREEN)
    elif repetitions == 2 or repetitions == 4 or repetitions == 6:
        count_down(SHORT_BREAK_MIN * 60)
        label.config(text="Break", fg=PINK)
    elif repetitions == 8:
        count_down(LONG_BREAK_MIN * 60)
        label.config(text="Break", fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    
    if seconds < 10:
        seconds = f"0{seconds}"
        
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    
    if count > 0:
        window.after(1000, count_down, count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 30, "normal"), fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)   # Create a Canvas Widget with W and H similar to the image
tomato_img = PhotoImage(file="day28/tomato.png") # Read the image file
canvas.create_image(100, 112, image=tomato_img)   # Create image with 1/2canvas_width and 1/2canvas_Height to put the image in the center
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  # Create text in the center of the canvas
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

checkmark = Label(text="✔", fg=GREEN, font=(FONT_NAME, 24, "bold"), bg=YELLOW)
checkmark.grid(column=1, row=3)




window.mainloop()