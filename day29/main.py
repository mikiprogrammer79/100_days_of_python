from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas padding 20px W: 200 H: 200
img = PhotoImage(file="day29/logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=3, highlightbackground="black")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# Labels and Entries
website = Label(text="Website:")
website.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1)

user_name = Label(text="Email/Username:")
user_name.grid(column=0, row=2)
user_entry = Entry(width=35)
user_entry.grid(column=1, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)



window.mainloop()
