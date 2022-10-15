import random
import os

clear = lambda: os.system('cls')

def play():
    start_game = input("type y to play: ")
    if start_game == "y":
        guess_number()
    else:
        print("Move along then")

def mode():
    game_mode = input("easy or hard? ")
    guesses = 0
    if game_mode == "easy":
        guesses += 10
    elif game_mode == "hard":
        guesses += 5 
    return guesses
    
def check_answer(random_number,guesses, user_guess):
    if user_guess == random_number:
        print(f"{user_guess} is correct! play again?")
        play()
    elif user_guess > random_number:
        print(f"{user_guess} is too high, try again")
        return
    elif user_guess < random_number:
        print(f"{user_guess} is too low, guess again")
        return

def guess_number():
    clear()
    random_number = random.randint(1,100)
    guesses = mode()
    while guesses > 0:
        print(f"you have {guesses} attempts remaining")
        user_guess = int(input("Guess a number between 1 and 100: "))
        clear()
        check_answer(random_number,guesses, user_guess)
        guesses -= 1
    if guesses == 0:
        print("you're out of guesses, you lose")
    play()
    print("Thank you for playing")


print("Welcome to guess a number!")
play()

       

