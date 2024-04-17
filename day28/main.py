from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")

canvas = Canvas(width=200, height=224)   # Create a Canvas Widget with W and H similar to the image
tomato_img = PhotoImage(file="day28/tomato.png") # Read the image file
canvas.create_image(100, 112, image=tomato_img)   # Create image with 1/2canvas_width and 1/2canvas_Height to put the image in the center
canvas.pack()




window.mainloop()