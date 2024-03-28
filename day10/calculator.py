# Python Calculator

def start():
    print('''
 _____________________
|  _________________  |
| | PY           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

          ''')

def add(a, b):
    sum = a + b
    return sum
def sub(a, b):
    sub = a - b
    return sub
def mult(a, b):
    mult = a * b
    return mult
def div(a, b):
    div = a / b
    return div
def exp(a, b):
    exp = a ** b
    return exp

# Create operators/operations dictionary
operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
    "**": exp,
}

start()

# Prompt the user to type a number
number1 = float(input("First number: "))
# Show user different operators
for operator in operations:
    print(operator)
memory = [number1]
alive = True
while alive:
    # Prompt the user to pick up an operator
    user_operator = input("Pick up an operator: ")
    # Prompt user to type second number
    number2 = float(input("Next number: "))
    # Calculator
    result = operations[user_operator](memory[-1], number2) # add/sub/mult/div/exp(a, b)
    print(f"{memory[-1]} {user_operator} {number2} = {result}")

    # Prompt the user to continue or exit
    if input(f"Type 'y' to continue calculating with {result}. Press Enter for exit: ").lower() == "y":
        memory.append(result)
    else:
        alive = False