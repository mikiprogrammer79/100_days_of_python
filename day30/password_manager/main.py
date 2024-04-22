from tkinter import *
from tkinter import messagebox  # messagebox is not a class
import random
import string
import pyperclip  # To auto copy/paste clipboard functions
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_password():
    password_entry.delete(0, END)
    letters_num = 8
    symbols_num = 4
    numbers_num = 4
    
    letter_list = list(string.ascii_letters)
    user_letters = []
    for i in range(0, letters_num):
        random_number = random.randint(0, (len(letter_list) -1))
        user_letters.append(letter_list[random_number])
    
    symbol_list = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "?", "/", "+", "="]
    user_symbols = []
    for i in range(0, symbols_num):
        random_number = random.randint(0, (len(symbol_list) - 1))
        user_symbols.append(symbol_list[random_number])
    
    number_list = list(string.digits)
    user_numbers = []
    for i in range(0, numbers_num):
        random_number = random.randint(0, (len(number_list) - 1))
        user_numbers.append(number_list[random_number])
    
    password = user_letters + user_symbols + user_numbers
    shuffle_passwd = random.shuffle(password) 
    new_password = "".join(password)

    password_entry.insert(0, f"{new_password}")
    pyperclip.copy(new_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    site = website_entry.get()
    email = user_entry.get()
    passwd = password_entry.get()

    # Create dictionary to Read, Write and Update JSON data
    new_data = {
        site: {
            "email": email,
            "password": passwd,
        }
    }

    if site == "" or passwd == "" or email == "": 
        messagebox.showinfo(title="Oops", message="Please, do not leave any field empty!")
        info = False
    else:
        info = messagebox.askokcancel(title=site, message=f"Are these details ok?\nEmail: {email}\nPassword: {passwd}")
    
        if info:
            try:
                # Reading old data
                with open("day30/password_manager/data.json", mode="r") as data_file:
                    data = json.load(data_file)
                # Updating old data as new data
                    data.update(new_data)
            except FileNotFoundError:
                data = new_data
                
            finally:
                # Write updated data
                with open("day30/password_manager/data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
    
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- PASSWORD FINDER ------------------------------- #
def find_password():
    site = website_entry.get()
    email = user_entry.get()
    passwd = password_entry.get()
    
    with open("day30/password_manager/data.json", mode="r") as data_file:
        data = json.load(data_file)
    
        if site in data:
            messagebox.showinfo(title=site, message=f"Email: {data[site]["email"]}\nPassword: {data[site]["password"]}")
        else:
            messagebox.showerror(title="Error", message="No details for the website exist")    

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
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky=W)

search = Button(text="Search", command=find_password, width=13)
search.grid(column=1, row=1, sticky=E)

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
generate_button = Button(text="Generate Password", command=gen_password)
generate_button.grid(column=1, row=3, sticky=E)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4)

window.mainloop()
