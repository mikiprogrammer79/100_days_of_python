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

start()

# Prompt the user to type a number
number1 = float(input("First number: "))
memory = [number1]
alive = True
while alive:
    # Prompt the user to pick up an operator
    user_operator = input("+\n-\n*\n/\n**\nPick up an operator: ")
    # Prompt user to type second number
    number2 = float(input("Next number: "))
    # Calculator
    result = 0
    if user_operator == "+":
        result = add(memory[-1], number2)
        print(f"{memory[-1]} + {number2} = {result}")
    elif user_operator == "-":
        result = sub(memory[-1], number2)
        print(f"{memory[-1]} - {number2} = {result}")
    elif user_operator == "*":
        result = mult(memory[-1], number2)
        print(f"{memory[-1]} * {number2} = {result}")
    elif user_operator == "/":
        result = div(memory[-1], number2)
        print(f"{memory[-1]} / {number2} = {result}")
    elif user_operator == "**":
        result = exp(memory[-1], number2)
        print(f"{memory[-1]}exp{number2} = {result}")
    else:
        print("Wrong operator")

    # Prompt the user to continue or exit
    if input(f"Type 'y' to continue calculating with {result}. Press Enter for exit: ").lower() == "y":
        memory.append(result)
    else:
        alive = False