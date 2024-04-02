from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

alive = True
while alive:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if prompt == "latte":
        menu_item = menu.menu[0]
    elif prompt == "espresso":
        menu_item = menu.menu[1]
    elif prompt == "cappuccino":
        menu_item = menu.menu[2]

    # Print report
    if prompt == "report":
        coffee.report()
    elif prompt == "latte" or prompt == "cappuccino" or prompt == "espresso":
        # check resources sufficient?
        if coffee.is_resource_sufficient(menu_item):
            # Process coins
            enough_coins = money.make_payment(menu_item.cost)
            # Check transaction successful
            while not enough_coins:
                money.make_payment(menu_item.cost)
            # Make coffee
            coffee.make_coffee(menu_item)

    elif prompt == "exit":
        alive = False        
    else:
        print("Wrong item. Try again")