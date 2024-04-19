# Prevent the program from crashing. 
# If the user enters something that is out of range 
# just print a default output of "Fruit pie".

fruits = input("Type a list of fruits separated by coma: ").split()

# TODO: Catch the exception and make sure the code runs without crashing.

def make_pie(index):
    try:
      fruit = fruits[index]
    except IndexError:
      print("Fruit pie")
    else:
      print(fruit + " pie")

make_pie(7)
