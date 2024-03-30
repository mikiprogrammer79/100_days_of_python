# FizzBuzz Game

# Print each number from 1 to 100 in turn and include number 100.
for number in range(1, 101):
  # if the number is divisible by both 3 and 5 -> "FizzBuzz"
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  # When the number is divisible by 3 -> "Fizz".
  elif number % 3 == 0:
    print("Fizz")
  # When the number is divisible by 5 -> "Buzz".
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
    