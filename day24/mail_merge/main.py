# Create a letter using starting_letter.docx
# for each name in invited_names.txt:
# Replace the name place holder with the actual name.
# Save the letter in the folder "ReadyToSend"


# Read names
with open("day24/mail_merge/Input/Names/invited_names.txt") as names:
    name_read = names.read()

names_list = name_read.split()

# Read starting_letter.txt first line and replace place holder. Then write letter
for name in names_list:
    with open("day24/mail_merge/Input/Letters/starting_letter.txt") as starting_letter:
        #blueprint = starting_letter.read()
        line = starting_letter.readline()
        place_holder = line.replace("[name]", name)
        letter_body = starting_letter.read()
        with open(f"day24/mail_merge/Output/ReadyToSend/{name}.txt", mode="w") as letter:
            letter.write(f"{place_holder}{letter_body}")    
