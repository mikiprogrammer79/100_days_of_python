# pack(); place(); grid()

from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    label.config(text=new_text)

def new_button_clicked():
    print("New button clicked")
    label.config(text="Beautiful!!!!")


# Window    
window = Tk()
window.title("Pack, Place, Grid GUI program examples")
window.minsize(width=500, height=300)
window.config(padx=20, pady=10) # Add padding 


# Label
label = Label(text="My text label", font=("Arial", 18, "bold"))
label.config(padx=20, pady=20) # Add padding
# label.pack(side="left")
label.place(x=200, y=150)

# Button
button = Button(text="Click here", command=button_clicked)
# button.pack()
button.grid(column=0, row=0)

# Entry
input = Entry(width=30)
# input.pack()
input.grid(column=3, row=1)

# New button
new_button = Button(text="Say Beautiful", command=new_button_clicked)
new_button.grid(column=3, row=3)





window.mainloop()