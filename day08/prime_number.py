# Prime Number Checker

print("Welcome to the Python Prime Number Checker!!")
print("Prime numbers are numbers that can only be cleanly divided by themselves and 1.")

# Prompt the user to enter a number
user_number = int(input("Let's try one number: "))

# Prime checker
# A prime is a natural number > 1 that is not a product of two smaller natural numbers.
def prime_checker(n):
    prime_test = []
    if n == 2 or n == 3:
        print("It's a prime number.")
    elif n >= 4:
        for i in range(2, n):
            if n % i == 0:
                prime_test.append(False)
        if False in prime_test:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")
    else:
        print("It's not a prime number.")

# Check user number
prime_checker(user_number)