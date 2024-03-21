# BMI Calculator version 2.0
# Body Mass Index (BMI) based on a user's weight and height.
# Interpretation based on the BMI value (Dr. Yu):
    # Under 18.5 they are underweight
    # Equal to or over 18.5 but below 25 they have a normal weight
    # Equal to or over 25 but below 30 they are slightly overweight
    # Equal to or over 30 but below 35 they are obese
    # Equal to or over 35 they are clinically obese.

print("Welcome to the Body Mass Index (BMI) calculator version 2.0!")

#Prompt the user to enter his height in meters (Float number)
height = float(input("Enter your height in meters: "))

#Prompt the user to enter his weight in kilograms (Integer number)
weight = int(input("Enter your weight in kilograms: "))

#Calculate BMI
bmi = weight / height ** 2
f_bmi = format(bmi, '.2f')
#Assign interpretation based on the BMI value
if bmi < 18.5:
    print(f"Your BMI is {f_bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {f_bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {f_bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {f_bmi}, you are obese.")
else:
    print(f"Your BMI is {f_bmi}, you are clinically obese.")
