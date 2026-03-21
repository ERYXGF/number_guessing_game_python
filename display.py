"""Contains all terminal output functions: the welcome screen, the difficulty menu, the board display after each guess, the win screen, the loss screen and the scores display. Nothing in this file does any logic — it only prints."""

#Function that displays the welcome screen:
def welcome_screen():
    print("Hello, Welcome to the Number Guessing game !")
    print("Do you want to:")
    print("1) Play a game")
    print("2) View high score")
    print("3) View all saved scores")
    print("4) Quit")

#Function that displays the difficulty menu:
def difficulty_display():
    print("Please select one of the difficulties below:")
    print("1) Easy: Number between 0 and 50")
    print("2) Medium: Number between 0 and 100")
    print("3) Hard: Number between 0 and 200")

#Function that creates the board display after each move:
def board_display(max_range, remaining_attempts, hint):
    print("You have not guessd the correct number,")
    print(f"You have {remaining_attempts} attempts remaining.")
    print(f"The number you're looking for is between 0 and {max_range}")
    print(f"{hint}")


#Function that displays the win screen:
def win_screen(difficulty, attempts, new_record = False):
    print(f"Congratulations ! You have won on {difficulty} !")
    print(f"Attempts used : {attempts}")
    if new_record == True:
        print("Congratulations ! You just Broke a new record !")

#Function that displays the loss screen:
def loss_screen(secret, guess_diff):
    print("Unfortunately, you lost. Restart the game to try your luck again !")
    print(f"You guess was close, {guess_diff} away from the secret number")
    print(f"The secret number was {secret}")

#Function that does the score display:
def score_display(scores, difficulty):
    print("Here are your scores so far: ")
    print(f"You current best attempt is : {scores['best_attempts']}")
    print(f"The date of your best attempt was : {scores['date']}")
    print(f"The difficulty chosen was : {difficulty}")

#Function that shows the score theyre trying to beat on a specific difficulty:
def scores_before_game(record, difficulty):
    print(f"Your current record for the {difficulty} difficulty level is {record}")