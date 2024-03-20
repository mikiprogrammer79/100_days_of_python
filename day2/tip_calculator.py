print("Welcome to the tip calculator!")

# Prompt the user to type the total bill
bill = input("What was the total bill?\n$")

# Prompt the user to choose how much tip
tip = input("How much tip would you like to give? 10, 12, or 15 percent?\n%")

# Prompt the user to type how many people to split the bill

num_people = input("How many people to split the bill?\n")

# Calculate how much each person should pay
total_bill = float(bill) + (int(tip) / 100) * float(bill) # print(type(total_bill)) <class 'float'>
each_person_bill = total_bill / int(num_people)
print(f"Each person should pay: ${round(each_person_bill, 2)}")

