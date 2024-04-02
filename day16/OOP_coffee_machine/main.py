from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

alive = True
while alive:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # Print report
    if prompt == "report":
        coffee.report()
    elif prompt == "latte" or prompt == "cappuccino" or prompt == "espresso":
        # check resources sufficient?
        if coffee.is_resource_sufficient(menu.find_drink(prompt)):
            # Process coins
            enough_coins = money.make_payment(menu.find_drink(prompt).cost)
            # Check transaction successful
            while not enough_coins:
                money.make_payment(menu.find_drink(prompt).cost)
            # Make coffee
            coffee.make_coffee(menu.find_drink(prompt))

    elif prompt == "exit":
        alive = False        
    else:
        print("Wrong item. Try again")