# Prompt user to type different values of student heights
student_heights = input("Input a list of student heights separated with one space. Example: 120 130\n").split()

# Conver string input into a list of integer numbers 
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# Calculate the average height
sum = 0
for item in student_heights:
  sum += item

print(f"total height = {sum}\nnumber of students = {len(student_heights)}")
print(f"average height = {round(sum / len(student_heights))}")