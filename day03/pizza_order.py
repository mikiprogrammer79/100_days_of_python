print("Welcome to pizza_order.py and take an automatic pizza order!!")

size = input("What size pizza do you want? S, M, or L ").lower() # Prompt size 
add_pepperoni = input("Do you want pepperoni? Y or N ").lower() # Prompt user if he wants peperoni 
extra_cheese = input("Do you want extra cheese? Y or N ").lower() # Prompt user to add extra cheese

# PRICE TABLE:
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

bill = 0
if size == "s":
    bill = 15
    if add_pepperoni == "y":
        bill += 2
elif size == "m":
    bill = 20
    if add_pepperoni == "y":
        bill += 3
elif size == "l":
    bill = 25
    if add_pepperoni == "y":
        bill += 3
else:
    print(f"ErrorSize, we do not make \"{size.upper()}\" size")

if extra_cheese == "y":
    bill += 1

format_bill = format(bill, '.2f')

print(f"Thank you for choosing pizza_order.py! Your final bill is: ${format_bill}.")