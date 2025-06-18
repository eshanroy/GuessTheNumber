import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 5
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100. You have 5 attempts.")

    for i in range(attempts):
        try:
            guess = int(input(f"\nAttempt {i+1}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == number_to_guess:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("Too high!")
    else:
        print(f"\n Game Over! The number was {number_to_guess}.")

number_guessing_game()