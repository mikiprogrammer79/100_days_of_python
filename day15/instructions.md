# Coffee Machine
## 1. Make 3 hot flavours:
    A. Expresso (50ml water; 18g coffee; $1.50)
    B. Latte (200ml water; 24g coffee; 150ml milk; $2.50)
    C. Cappuccino (250ml water; 24g coffee; 100ml milk; $3.00)
## 2. Coffee Machine Resources:
    Water: 300ml
    Milk: 200ml
    Coffee: 100g
## 3. Coin operated:
    Penny: 1 cent 
    Nickel: 5 cents 
    Dime: 10 cents 
    Quarter: 25 cents 

## Pseudo-code:
## Prompt (What would you like? (espresso/latte/cappuccino): )
###    report -> Show all resources left in the machine
###    cls -> Clear screen
###    espresso/latte/cappuccino
        A. Check there are sufficient resources
        B. If resources, "Please, insert coins"
        C. If coins inserted > price -> make coffee and calculate change
