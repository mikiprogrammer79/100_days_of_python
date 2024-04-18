from tkinter import *
from tkinter import messagebox  # messagebox is not a class

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    site = website_entry.get()
    email = user_entry.get()
    passwd = password_entry.get()

    if site == "" or passwd == "" or email == "": 
        messagebox.showinfo(title="Oops", message="Please, do not leave any field empty!")
        info = False
    else:
        info = messagebox.askokcancel(title=site, message=f"Are these details ok?\nEmail: {email}\nPassword: {passwd}")
    
        if info:
            with open("day29/data.tx", mode="a") as file:
                file.write(f"{site} | {email} | {passwd}\n")
    
        website_entry.delete(0, END)
        password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas padding 20px W: 200 H: 200
img = PhotoImage(file="day29/logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=3, highlightbackground="black")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# Labels and Entries
website = Label(text="Website:")
website.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky=W)

user_name = Label(text="Email/Username:")
user_name.grid(column=0, row=2)
user_entry = Entry(width=35)
user_entry.insert(0, "your_email@gmail.com")
user_entry.grid(column=1, row=2, sticky=W)

password = Label(text="Password:")
password.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky=W)

# Buttons
generate_button = Button(text="Generate Password")
generate_button.grid(column=1, row=3, sticky=E)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4)

window.mainloop()
