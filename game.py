"""Contains the core game logic. The main game loop lives here: generating the secret number, managing the attempt counter, calling hint functions, checking for win or loss, returning the result. This is the largest file."""

#Random module for the core function:
import random

#Import higher/lower func and cold/hot func from hints.py:
from hints import higher_lower
from hints import hot_cold

#Import all the functions in display.py to be able to use them here:
from display import welcome_screen, difficulty_display, board_display, win_screen, loss_screen, score_display, scores_before_game

#Imports score.py to be used here:
from scores import check_record

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
def core_loop(level, difficulty):
    #Generates + stores random number:
    rand_num = random.randrange(*level["range"])
    #Establish attempt counter:
    attempts = level["attempts"]
    #While loop that encompasses everything:
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
            win_screen(difficulty, attempts, new_record = check_record(attempts+1, difficulty))
            return True
        else:
            #Define hint to be used in the board_display function:
            hint = (f"{higher_lower(rand_num, guess)}, {hot_cold(rand_num, guess, level)}")
        #Check how many attempts are left
            if attempts > 0:    
                board_display(level["range"][1], attempts, hint)
            else:
                loss_screen(rand_num, abs(guess-rand_num))
                return False
