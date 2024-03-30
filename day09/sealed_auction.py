# Python FPSBA
# A first-price sealed-bid auction (FPSBA) is a common type of auction. Also known as blind auction. 
# All bidders simultaneously submit sealed bids so that no bidder knows the bid of any other participant. 
# The highest bidder pays the price that was submitted.

import os

def start():
    print('''
                           ___________
                           \         /
                            )_______(
                            |"""""""|_.-._,.---------.,_.-._
                            |       | | |               | | ''-.
                            |       |_| |_             _| |_..-'
                            |_______| '-' `'---------'` '-'
                            )"""""""(
                           /_________\(Silence!!)
                            
                         .-------------.
                        |_______________|
        ''')
    print("Welcome to the Fist-Price Sealed-Bid Auction Program!")

# Create a bidder dictionary
bidder_dict = {}
# Keep propmting while auction alive 
alive = True
while alive:
    start()
    name = input("What's your name?: ").capitalize()
    bid = input("What's your bid?: ")

    # Add name and bid to bidder_dict
    bidder_dict[name] = bid

    # Prompt the user if there are any other bidders
    typo = True
    while typo:
        more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        if more_bidders == "no":
            alive = False
            typo = False
            os.system("clear")
            bidder_values = []
            for key in bidder_dict:
                bidder_values.append(bidder_dict[key])
            max_bid = max(bidder_values)
            name = ""
            for key in bidder_dict:
                if bidder_dict[key] == max_bid:
                    name = key
            print(f"The winner is {name} with a bid of ${max_bid}")
        elif more_bidders == "yes":
            typo = False
            os.system("clear")
        else:
            typo = True
