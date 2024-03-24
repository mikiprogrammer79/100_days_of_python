# Password Generator
import random
import string

print("Welcome to the Python Password Generator!")

# Prompt the user to input how many letters 
letters_num = int(input("How many letters would you like in your password? "))

# Prompt the user to input how many symbols
symbols_num = int(input("How many symbols would you like in your password? "))

# Prompt the user how many numbers
numbers_num = int(input("How many numbers would you like in your password? "))

# Get Letters
letter_list = list(string.ascii_letters)
# user_letters = []
# for i in range(0, (letters_num + 1)):
#     random_number = random.randint(0, (len(letter_list) -1))
#     user_letters.append(letter_list[random_number])
# letters = "".joint(user_letters)
print(letter_list)