# Number Guessing Project

import art
import random

def entry_validation(guess):
    while guess < 1 or guess > 100:
        guess = int(input("Invalid number. Please type again. "))
    return guess

def play_game():
    print(art.logo)
    level = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard': ").lower()


    answer = random.randint(1, 101)
    print(answer)

    guess = 0
    n = 0

    if level == "easy":
        n = 10

    if level == "hard":
        n = 5

    print(f"You have {n} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))
    entry_validation(guess)

    for attempt in range(n-1):
        print(f"You have {(n-1) - attempt} attempts remaining to guess the number.")
        if answer > guess:
            guess = int(input("Too low.\nGuess again: "))
            entry_validation(guess)
        elif answer < guess:
            guess = int(input("Too high.\nGuess again: "))
            entry_validation(guess)
        else:
            break

    if guess == answer:
        print(f"You got it! The answer is {answer}!")
    else:
        print("You've run out of guesses. You lose.")


play_game()