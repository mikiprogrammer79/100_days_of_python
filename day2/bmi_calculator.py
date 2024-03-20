# The BMI is calculated by dividing an adult's weight in kilograms by their height in metres squared.
# Kg/m2

print("Your BMI result will be displayed as int(number) with one of these weight categories:")
print("- underweight: <18.5")
print("- a healthy weight: 18.5 - 24.9")
print("- overweight: 25 - 29.9")
print("- obese: >= 30")

# First input: weight in kilograms
weight = input("What's your weight in kilograms(kg)? \n")

# Second input: height in meters
height = input("What's your height in meters(m)? \n")

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
bmi = float(weight) / float(height) ** 2

print(int(bmi))


