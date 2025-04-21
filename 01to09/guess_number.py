import random

def guess(x):
    number = random.randint(1, x)
    while True:
        user_guess = int(input(f"Guess a number between 1 and {x}: "))
        if user_guess < number:
            print("Too low!")
        elif user_guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the correct number: {number}")
            break

guess(10)
