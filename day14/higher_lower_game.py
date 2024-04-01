# Higher Lower Game

import random
import os
import game_data

# ASCII Art
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
# Get random person
def random_person(index, option):
    name = game_data.data[index]["name"]
    description = game_data.data[index]["description"]
    country = game_data.data[index]["country"]    
    print(f"Compare {option}: {name}, {description} from {country}")

# Print Question
def question(index_a, index_b):
    # Print option_a
    random_person(index_a, "A")
    # Print vs
    print(vs)
    # Print option_b
    random_person(index_b, "B")

# Check answer
def check_answer(index_a, index_b, answer):
    global score
    global alive
    global random_index
    followers_a = game_data.data[index_a]["follower_count"]
    followers_b = game_data.data[index_b]["follower_count"]
    if answer == "A" and followers_a > followers_b:
        score += 1
        random_index = index_b
        os.system("clear")
        print(logo)
        print(f"You are right. Current score: {score}")
    elif answer == "B" and followers_b > followers_a:
        score += 1
        random_index = index_b
        os.system("clear")
        print(logo)
        print(f"You are right. Current score: {score}")
    else:
        alive = False
        print(f"Sorry, you are wrong.\nA: {followers_a}M followers\nB: {followers_b}M followers\nScore: {score}")

# Initial score
score = 0

# Get a random index
random_index = random.randint(0, (len(game_data.data) - 1))

# Print logo
print(logo)

# while game flag is alive:
alive = True
while alive:
    random_b = random.randint(0, (len(game_data.data) - 1))
    # Print question
    question(random_index, random_b)
    
    # Prompt user to answer question
    user_answer = input("Who has more followers? Type 'A' or 'B': ").upper() 

    # Check answer
    check_answer(random_index, random_b, user_answer)