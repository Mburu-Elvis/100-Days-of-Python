import random
import art

DIFFICULT = 5
EASY = 10

def set_difficulty(level):
    if level == 'easy':
        guesses = EASY
    else:
        guesses = DIFFICULT
    return guesses

def check_number(num, guess):
    if guess < num:
        print("Too low.")
        return False
    elif guess > num:
        print("Too high.")
        return False
    else:
        print(f"You got it! The answer was {num}")
        return True

def number_guessing():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    guesses = set_difficulty(difficulty)
    number = random.randint(1, 100)

    while guesses > 0:
        print(f"You have {guesses} attempts remaining to guess the number.")
        user_guess = int(input("Guess number: "))
        if check_number(number, user_guess) == False:
            guesses -= 1
            continue
        else:
            break
    if guesses == 0:
        print("You've run out of guesses, you lose.")

print(art.logo)
number_guessing()