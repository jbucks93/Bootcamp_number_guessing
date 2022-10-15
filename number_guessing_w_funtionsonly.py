import random

def check_answer(guess, answer):
    if guess == answer:
        print("Correct")
    elif guess > answer:
        print("Too high, try again")
    elif guess < answer:
        print("Too low, guess again")

def mode():
    game_mode = input("easy or hard? ")
    if game_mode == "easy":
        return EASY_MODE
    elif game_mode == "hard":
        return HARD_MODE

EASY_MODE = 10
HARD_MODE = 5
playing = True
print("")

while playing:
    guesses = mode()
    guess = int(input("Guess a number between 1 and 100: "))
    answer = random.randint(1, 100)
    check_answer(guess, answer)
    guesses -=1
