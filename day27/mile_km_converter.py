# Miles to Kilometers Converter

from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=10, pady=10)

# Entry Miles
entry = Entry(width=10)
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
km.grid(column=2, row=1)







window.mainloop()