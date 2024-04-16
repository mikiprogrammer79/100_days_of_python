# Miles to Kilometers Converter

from tkinter import *


def convert():
    input = entry.get()
    kilometers = round(int(input) * 1.609, 2)
    value.config(text=kilometers)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=10, pady=20)

# Entry Miles
entry = Entry(width=10)
entry.focus()   # Puts cursor in entry
entry.grid(column=1, row=0)


# Label "Miles"
miles = Label(text="Miles", font=("Courier", 14, "normal"))
miles.grid(column=2, row=0)

# Label "is equal to"
equal = Label(text="is equal to", font=("Courier", 14, "normal"))
equal.grid(column=0, row=1)

# Label value
value = Label(text="0", font=("Courier", 20, "bold"))
value.grid(column=1, row=1)

# Label Km
km = Label(text="Km", font=("Courier", 14, "normal"))
km.config(padx=0, pady=20)
km.grid(column=2, row=1)

# Button Calculate
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)






window.mainloop()