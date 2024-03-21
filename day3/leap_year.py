# This program that works out whether if a given year is a leap year. 
# A normal year has 365 days, leap years have 366, with an extra day in February. 
# A leap year:
    # on every year that is divisible by 4 with no remainder
    # except for end-of-century years, unless the year is also divisible by 400 with no reminder

print("Welcome to leap_year.py! Check if a given year is a leap year.")

# Prompt the user what year he wants to check
year = int(input("What year do you want to check? "))

# Conditional statements (Control Flow)
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year}: Leap year")
        else:
            print(f"{year}: Not leap year")
    else:
        print(f"{year}: Leap year")
else:
    print(f"{year}: Not leap year")
