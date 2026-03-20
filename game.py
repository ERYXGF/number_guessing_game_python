"""Contains the core game logic. The main game loop lives here: generating the secret number, managing the attempt counter, calling hint functions, checking for win or loss, returning the result. This is the largest file."""

#Random module for the core function:
import random
#Import higher/lower func and cold/hot func from hints.py:
from hints import higher_lower
from hints import hot_cold

#"Difficulty" Dictionnary that defines each level of difficulty (number of attempts, range and hint precision/thresholds):
difficulty = {
    "easy": {
        "range": (1, 50),
        "attempts": 10,
        "thresholds": [
            (3,  "🔥 Brûlant"),
            (8,  "♨️  Très chaud"),
            (15, "🌡  Chaud"),
            (25, "❄️  Froid"),
        ]
    },
    "medium": {
        "range": (1, 100),
        "attempts": 7,
        "thresholds": [
            (5,  "🔥 Brûlant"),
            (15, "♨️  Très chaud"),
            (30, "🌡  Chaud"),
            (50, "❄️  Froid"),
        ]
    },
    "hard": {
        "range": (1, 200),
        "attempts": 5,
        "thresholds": [
            (10,  "🔥 Brûlant"),
            (30,  "♨️  Très chaud"),
            (60,  "🌡  Chaud"),
            (100, "❄️  Froid"),
        ]
    }
}

#Function that establishes the core game loop: generates random number, asks for a guess in while loop, checks if its correct, decrements attempts and detects losses:
def core_loop(level):
    #Generates + stores random number:
    rand_num = random.randrange(*level["range"])
    #Establish attempt counter:
    attempts = level["attempts"]
    while True:
        #Get the user's guess
        while True:
            try:
                guess = int(input("Please take a guess: "))
                break
            except ValueError:
                print("This is not a valid guess. Please guess again: ")
        #Take off guess from the attempt counter   
        attempts -= 1
        #Check if the users guess is right:
        if guess == rand_num:
            print("You have guessed correctly !")
            return True
        else:
        #Check how many attempts are left
            if attempts > 0:    
                print("You have guessed incorrectly. Please guess again: ")
                print(hot_cold(rand_num, guess, level))
                print(higher_lower(rand_num, guess))
            else:
                print("You have exceeded the total number of guesses you had. Play another round to try your luck again.")
                return False
