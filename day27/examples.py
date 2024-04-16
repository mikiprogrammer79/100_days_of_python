import tkinter

# Create windows and labels
# Window
window = tkinter.Tk()

window.title("Examples window.title") # Set windows title

window.minsize(width=500, height=300) # Define minimum size of the window

# Label
my_label = tkinter.Label(text="This is my label", font=("Arial", 24, "bold")) 
my_label.pack() # Put the label on the screen

# Play with Unlimited *args function. Adding as many numbers as we want
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

result = add(1, 2, 3, 4, 10, 40, 30, 11) # -> 101

print(result)

# Change label text
my_label["text"] = "This is a new label text"

my_label.config(text="This is another label text")

# Create a button
def button_clicked():
    print("Button clicked")
    my_label["text"] = "Button got clicked" # Change label text when button clicked
    my_label.config(text=input_box.get())
button = tkinter.Button(text="click here", command=button_clicked)
button.pack()

# Add an input field with Entry()
input_box = tkinter.Entry(width=10)
input_box.pack()

# Entries
entry = tkinter.Entry(width=30)
entry.insert(tkinter.END, string="Type your email here")
print(entry.get()) # Get text in entry
entry.pack()

# Text box
text = tkinter.Text(height=5, width=30)
text.focus() # Puts cursor in text box
text.insert(tkinter.END, "Type your message here")
print(text.get("1.0", tkinter.END)) # Text starts at line 1, character 0
text.pack()

# Spinbox
def spinbox_value():
    print(spinbox.get()) # Print the spinbox value

spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_value)
spinbox.pack()

# Scale
def scale_value(value):
    print(value)

scale = tkinter.Scale(from_=0, to=10, command=scale_value)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()





window.mainloop() # Keep the window on screen and listening

