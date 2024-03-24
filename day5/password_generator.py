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

# Get Letters (string.ascii_letters)
letter_list = list(string.ascii_letters)
user_letters = []
for i in range(0, letters_num):
    random_number = random.randint(0, (len(letter_list) -1))
    user_letters.append(letter_list[random_number])
# letters = "".join(user_letters)

# Get symbols 
symbol_list = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "?", "/", "+", "="]
user_symbols = []
for i in range(0, symbols_num):
    random_number = random.randint(0, (len(symbol_list) - 1))
    user_symbols.append(symbol_list[random_number])
# symbols = "".join(user_symbols)

# Get numbers (string.digits)
number_list = list(string.digits)
user_numbers = []
for i in range(0, numbers_num):
    random_number = random.randint(0, (len(number_list) - 1))
    user_numbers.append(number_list[random_number])
# numbers = "".join(user_numbers)

# Generate Password / Shuffel password characters (random.shuffle)
password = user_letters + user_symbols + user_numbers
shuffle_passwd = random.shuffle(password) 
new_password = "".join(password)

print(f"Your new password: {new_password}")




