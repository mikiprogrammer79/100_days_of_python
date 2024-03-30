import random

# ROCK PAPER SCISSORS GAME
print("Welcome to Rock Paper Scissors Game")

# Rules
print("You can find the 'official' rules of the game on the website: https://wrpsa.com/")

# ASCII art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Prompt the user to choose between rock, paper, and scissors
user_input = input("Type your choice: \"R\" for 'Rock', \"P\" for 'Paper', or \"S\" for 'Scissors': ").lower()

# Machine random choice
options = [rock, paper, scissors]
random_index = random.randint(0, (len(options) - 1))
machine_choice = options[random_index]

# Game logic
win = "Yes, you win!!"
even = "Even! Try again"
lose = "Sorry, you've lost the game"
if user_input == "r":
    if random_index == 0:
        print(rock + "\nYou chose 'Rock'\n" + machine_choice + "\nMachine chose 'Rock'\n" + even)
    elif random_index == 1:
        print(rock + "\nYou chose 'Rock'\n" + machine_choice + "\nMachine chose 'Paper'\n" + lose)
    elif random_index == 2:
        print(rock + "\nYou chose 'Rock'\n" + machine_choice + "\nMachine chose 'Scissors'\n" + win)
    else:
        print("IndexError")
elif user_input == "p":
    if random_index == 0:
        print(paper + "\nYou chose 'Paper'\n" + machine_choice + "\nMachine chose 'Rock'\n" + win)
    elif random_index == 1:
        print(paper + "\nYou chose 'Paper'\n" + machine_choice + "\nMachine chose 'Paper'\n" + even)
    elif random_index == 2:
        print(paper + "\nYou chose 'Paper'\n" + machine_choice + "\nMachine chose 'Scissors'\n" + lose)
    else:
        print("IndexError")
elif user_input == "s":
    if random_index == 0:
        print(scissors + "\nYou chose 'Scissors'\n" + machine_choice + "\nMachine chose 'Rock'\n" + lose)
    elif random_index == 1:
        print(scissors + "\nYou chose 'Scissors'\n" + machine_choice + "\nMachine chose 'Paper'\n" + win)
    elif random_index == 2:
        print(scissors + "\nYou chose 'Scissors'\n" + machine_choice + "\nMachine chose 'Scissors'\n" + even)
    else:
        print("IndexError")
else:
    print("InputError: type 'R', 'P', or 'S' as input")
    