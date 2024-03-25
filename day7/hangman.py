# Hangman Game

import random
import os

words = ["greenkeeper", "beekeeper", "furniture", "diamond", "coffee"]

ascii_art = [
    '''
      _______
     |/      |
     |      
     |      
     |       
     |      
     |
 jgs_|___
    ''',
    '''
      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
 jgs_|___
    ''',
    '''
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
 jgs_|___
    ''',
    '''
      _______
     |/      |
     |      (_)
     |       |/
     |       |
     |      
     |
 jgs_|___
    ''',
    '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
 jgs_|___
    ''',
    '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      /
     |
 jgs_|___
    ''',
    '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / /
     |
 jgs_|___
    ''',
    ]

# Welcome to the game with logo
def logo():
    print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
      ''')

# Generate a random word
random_word = random.choice(words)

# Generate as many blanks as letters in word
blanks = []
for i in range(len(random_word)):
    blanks.append("_ ")


# Control Flow and logic of the game
game_alive = 0
while game_alive < 6:
    
    # Clear the screen and add logo
    os.system("clear")
    logo()
    print(ascii_art[game_alive])
    print("".join(blanks))
    # Ask the user to guess a letter
    user_guess = input("Guess a letter: ").lower()
    if user_guess in blanks:
        print(f"You've already used the letter {user_guess}. Try another one")
        user_guess = input("Guess a letter: ").lower()
    
    user_right = []
    
    # A. Check if the letter is in the random_word / else draw body part
    for i in range(0, len(random_word)):
        if random_word[i] == user_guess:
            blanks[i] = user_guess
            user_right.append("1")
        else:
            user_right.append("0")
    if "1" in user_right:
        if "_ " in blanks:
            print(ascii_art[game_alive])
            print("".join(blanks) + "\nWell done!")
        else:
            print("You win!!")
            game_alive = 10
    else:
        game_alive += 1
        print(ascii_art[game_alive])
        print("".join(blanks))
        print(f"Sorry, you're wrong. The letter {user_guess} is not in the word")
        
    
if game_alive == 6:
    print(ascii_art[6])
    print("Sorry, You've lost the game. Try again")