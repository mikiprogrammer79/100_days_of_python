# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas


#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

df = pandas.read_csv("day26/NATO_alphabet/nato_phonetic_alphabet.csv")

alpha_dict = {row.letter:row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

print(alpha_dict)