# Main Coffee Machine Program

import os
import cm_data


def main(command):
    # A. Check there are sufficient resources
    if check_resources(command):
        check_price(command)
        make_coffee(command)
    else:
        no_resources(command)


def check_resources(coffee):
    if cm_data.resources["water"] < cm_data.coffee_expenses[coffee]["water"]:
        return False
    elif cm_data.resources["milk"] < cm_data.coffee_expenses[coffee]["milk"]:
        return False
    elif cm_data.resources["coffee"] < cm_data.coffee_expenses[coffee]["coffee"]:
        return False
    else:
        return True


def check_price(coffee):
    price = cm_data.coffee_expenses[coffee]["price"]
    money_in = 0
    while price > money_in:
        print("Please, insert coins.")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))
        money_in += quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
        if price > money_in:
            print(f"You need to insert ${price - money_in} more")
        else:
            change = round(money_in - price, 2)
            print(f"Making your {coffee}...\nHere is ${change} in change") 


def make_coffee(coffee):
    cm_data.resources["water"] -= cm_data.coffee_expenses[coffee]["water"]
    cm_data.resources["milk"] -= cm_data.coffee_expenses[coffee]["milk"]
    cm_data.resources["coffee"] -= cm_data.coffee_expenses[coffee]["coffee"] 
    print(f"Here is your {coffee}. Enjoy!")
    # print(cm_data.resources)


def no_resources(coffee):
    for key in cm_data.resources:
        if cm_data.resources[key] < cm_data.coffee_expenses[coffee][key]:
            print(f"Sorry, there isn't enough {key}")
                  

power = True
while power:
    # Prompt user to enter a command:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
        main(prompt)
    elif prompt == "report":
        print(f"Water: {cm_data.resources['water']}ml")
        print(f"Milk: {cm_data.resources['milk']}ml")
        print(f"Coffee: {cm_data.resources['coffee']}g")
    elif prompt == "cls":
        os.system("clear")
        cm_data.resources["water"] = 300
        cm_data.resources["milk"] = 200
        cm_data.resources["coffee"] = 100
    elif prompt == "exit": 
        power = False
    else:
        print("Wrong command. Try again")    
