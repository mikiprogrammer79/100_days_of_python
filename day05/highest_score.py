# A program that calculates the highest score from a List of scores.
# To complicate the logic of the program the max() or min() functions are not allowed.

# Prompt the user to input a list of student scores
student_scores = input("Input a list of student scores").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Create a variable max_score to store the maximum scores
max_score = 0

# Control flow 
if student_scores[0] > student_scores[1]:
  max_score = student_scores[0]
else:
  max_score = student_scores[1]
for i in range(2, len(student_scores)):
  if max_score < student_scores[i]:
    max_score = student_scores[i]
  else:
    max_score = max_score

print(f"The highest score in the class is: {max_score}")