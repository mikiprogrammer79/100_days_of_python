# Number Guessing Game

import random

# Functions
def lose_attempt():
    global attempts
    attempts -= 1
    if attempts > 0:
        print("Guess again.")
        print(f"You have {attempts} attempts remaining to guess the number.")
    else:
        print("You've run out of guesses. You lose.") 


# Welcome to the Game
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Set difficulty and number of attempts
difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
elif difficulty == "hard":
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")

# Get a random number to be guessed
number = random.randint(1, 100)

while attempts > 0:
    # Prompt the user to make a guess
    user_guess = int(input("Make a guess: "))
    # Tell the user if the number guessed is Too high or Too low
    if user_guess > number:
        print("Too high")
        lose_attempt()
    elif user_guess == number:
        print(f"Yes {number} is the number, you win!!")
        attempts = 0
    else:
        print("Too low.")
        lose_attempt()
