# Caesar Cipher

import string
import os 

# Start the program
print('''
      _       _               
     (_)     | |              
  ___ _ _ __ | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|                    
      ''')

# Create alphabet list
alpha = list(string.ascii_letters)

# Encryption
def encode(message):
    alpha_index_list = []
    for i in range(0, len(message)):
        if message[i] in alpha:
            index = alpha.index(message[i])
            alpha_index_list.append(index)
        else:
            alpha_index_list.append(message[i])
    # print(alpha_index_list)
    encoded_list = []
    for item in alpha_index_list:
        if str(item).isnumeric():
            if (item + shift_number) > 51:
                new_index = item + shift_number - 52
                encoded_list.append(alpha[new_index])
            else:
                new_index = item + shift_number
                encoded_list.append(alpha[new_index])
        else:
            encoded_list.append(item)
    print(f'Encoded message: {"".join(encoded_list)}')

# Prompt the user to Encode or Decode a message
encryption_type = input("Type 'encode' to encrypt, or type 'decode' to decrypt:\n")
user_message = input("Type your message:\n")
shift_number = int(input("Type the shift number:\n"))

if encryption_type == "encode":
    encode(user_message)

