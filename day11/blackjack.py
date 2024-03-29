#Blackjack Game

import random
import os

# Create a function to print a card on the console
def print_card():
    rank_num = random.randint(1, 13)
    suits = suits_list[random.randint(0, 3)]
    space = space_value(rank_num)
    rank = ranks_dict[rank_num]

    lines = [[] for i in range(9)]

    lines[0].append('┌─────────┐')
    lines[1].append('│{}{}       │'.format(rank, space))  # space for ranks < 10
    lines[2].append('│         │')
    lines[3].append('│         │')
    lines[4].append('│    {}    │'.format(suits)) # ['♠', '♦', '♥', '♣']
    lines[5].append('│         │')
    lines[6].append('│         │')
    lines[7].append('│       {}{}│'.format(space, rank)) # space for ranks < 10
    lines[8].append('└─────────┘')

    for i in range(9):
        print("".join(lines[i]))

    memory.append(card_values(rank))

# Create start function to give to random cards to the user
def start():
    
    logo()
    
    rank_num = random.randint(1, 13)
    rank2_num = random.randint(1, 13)
    
    suits = suits_list[random.randint(0, 3)]
    suits2 = suits_list[random.randint(0, 3)]

    space = space_value(rank_num)
    space2 = space_value(rank2_num)
    rank = ranks_dict[rank_num]
    rank2 = ranks_dict[rank2_num]
            
    lines = [[] for i in range(9)]

    lines[0].append('┌─────────┐')
    lines[1].append('│{}{}       │'.format(rank, space))  # space for ranks < 10
    lines[2].append('│         │')
    lines[3].append('│         │')
    lines[4].append('│    {}    │'.format(suits)) # ['♠', '♦', '♥', '♣']
    lines[5].append('│         │')
    lines[6].append('│         │')
    lines[7].append('│       {}{}│'.format(space, rank)) # space for ranks < 10
    lines[8].append('└─────────┘')

    lines[0].append('┌─────────┐')
    lines[1].append('│{}{}       │'.format(rank2, space2))  # space for ranks < 10
    lines[2].append('│         │')
    lines[3].append('│         │')
    lines[4].append('│    {}    │'.format(suits2)) # ['♠', '♦', '♥', '♣']
    lines[5].append('│         │')
    lines[6].append('│         │')
    lines[7].append('│       {}{}│'.format(space2, rank2)) # space for ranks < 10
    lines[8].append('└─────────┘')

    print("Your cards:")

    for i in range(9):
        print("".join(lines[i][0]) + "".join(lines[i][1]))
    
    memory.append(card_values(rank) + card_values(rank2))

def space_value(num):
    if num == 10:
        return ''
    else:
        return ' '

def card_values(card):
    if card == "A":
        return 1
    elif card == "J" or card == "Q" or card == "K":
        return 10
    else:
        return int(card)


def logo():
    print('''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
                       _/ |                
                      |__/                
          ''')
# Create suits
suits_list = ['♠', '♦', '♥', '♣']
ranks_dict = {
    1: "A", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "J", 12: "Q", 13: "K",
}

# Scores
memory = [] # Store cards for accoutability

# Create a while loop for the game with flag alive
alive = True
while alive:
    start()
    machine_score = random.randint(17, 21)
    user_score = 0
    for item in memory:
        user_score += item
        print(item)

    on_hand = True
    while on_hand:
        prompt = input("Type 'y' to get another card, or hit 'Enter' to stand: ").lower()
    
        if prompt == "y":
            print_card()
            user_score += memory[-1]
            print(f"Your score: {user_score}")
            if user_score > 21:
                print(f"Sorry, you've been defeated.\nYour score: {user_score} is higher than 21")
                on_hand = False
                if input("Type 'y' to try again, or hit 'Enter' to exit: ").lower() == "y":
                    memory.clear()
                    os.system("clear")                
                else:
                    alive = False
                    print("Good Bye")
            
            elif user_score == 21:
                print("Blackjack!!!\nYou win!")
                on_hand = False
            
            else:
                on_hand = True        
        
        # No other hand, print results
        else:
            on_hand = False
            alive = False
            if user_score < machine_score:
                print(f"Sorry, you've been defeated.\nComputer score: {machine_score}\nYour score: {user_score}")
            
                if input("Type 'y' to try again, or hit 'Enter' to exit: ").lower() == "y":
                    alive = True
                    os.system("clear")
                    memory.clear()
            
            elif user_score > machine_score:
                print(f"Your score: {user_score}\nComputer score: {machine_score}\nYou win!")
                
            else:
                print(f"Your score {user_score} is equal to the computer score. Try again")
                memory.clear()