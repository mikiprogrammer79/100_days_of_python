line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? Line 1-3; Column A-C. Example B3: ") # Prompt the user to put the treasure

# map[lineX][lineX_index] = "X" position
line_index = 0
if "a" in position.lower():
  line_index = 0
elif "b" in position.lower():
  line_index = 1
elif "c" in position.lower():
  line_index = 2
else:
  print("CoordenateError")

row_index = 0
if "1" in position:
  row_index = 0
elif "2" in position:
  row_index = 1
elif "3" in position:
  row_index = 2
else:
  print("CoordenateError")

map[row_index][line_index] = " X"

# Print the map
print(f"{line1}\n{line2}\n{line3}")