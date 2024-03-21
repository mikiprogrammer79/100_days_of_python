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
        print("Ticket Price: $5.00")
    elif age <= 18:
        print("Ticket Price: $7.00")
    else:
        print("Ticket Price: $12.00")

else:
    print(f"Sorry, you are {height}cm tall. You need to grow {120 - height}cm more.")




