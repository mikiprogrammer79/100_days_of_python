# Paint Area Calculator
import math

print("Welcome to the paint area calculator!!")
print("The program will tell you how many cans of paint you need to paint your wall")

# prompt the user to input the Instructions of the paint manufacture
instructions = int(input("How many square meters can you do with one can of paint? Check Instructions: "))

# Prompt the user to input height and width of the wall
height_num = float(input("Type the height of the wall in meters (m): "))
width_num = float(input("Type the width of the wall in meters (m): "))

# Define a paint area calculator function
def paint_calc(height, width, coverage):
    cans_of_paint = (height * width) / coverage
    print(f"You will need {math.ceil(cans_of_paint)} cans of paint.")

# Call the function
paint_calc(height_num, width_num, instructions)

