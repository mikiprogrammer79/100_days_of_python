# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas


def alpha_code():
    user_input = input("Type a word or sentence: ").upper()
    try:
        phonetic_code = [alpha_dict[item] for item in user_input if item != " "]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        alpha_code()
    else:
        print(phonetic_code)



#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

df = pandas.read_csv("day26/NATO_alphabet/nato_phonetic_alphabet.csv")

alpha_dict = {row.letter:row.code for (index, row) in df.iterrows()}

#TODO 2. Call alpha_code() function 

alpha_code()


