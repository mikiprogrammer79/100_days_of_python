# This is a Roller Coaster ticketing program.
# The ticket price will be calculated according to age.
# Rules for a ride: The person should be 120cm tall at least.
# Price ticket: $5 (under 12 years old); $7 (between 12 and 18) and $12 (over 18).

print("Welcome to the rollercoaster!!")

# Prompt the user for his height
height = int(input("How tall are you? Please type your height in centimeters: "))

# Let the user know whether or not he is allowed for a ride
if height >= 120:
    print("Hi, you can ride!")
    # Prompt the user for his age and calculate the rollercoaster ticket price
    age = int(input("How old are you? "))
    if age < 12:
        print("Child Ticket Price: $5.00")
        ticket = 5.00
    elif age <= 18:
        print("Young Ticket Price: $7.00")
        ticket = 7.00
    else:
        print("Adult Ticket Price: $12.00")
        ticket = 12.00
    # Prompt the user to type Y or N in case they want a photo taken
    photo = input("Do you want a photo taken? Y or N: ").lower()
    if photo == "y":
        print(f"Total price: ${format(ticket + 3, '.2f')}") # Price for a photo taken $3.00
    else:
        print(f"Total price: ${format(ticket, '.2f')}")    
else:
    print(f"Sorry, you are {height}cm tall. You need to grow {120 - height}cm more.")




