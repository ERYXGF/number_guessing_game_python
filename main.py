""" Entry point only. Imports from all other files, runs the startup sequence and hands control to the game loop. Should be under 30 lines. Wires everything together: add the difficulty selection menu, play again prompt, and session statistics on exit."""

#Imports all the files that need to be used in the main func:
from game import core_loop, difficulty
from display import difficulty_display
from display import welcome_screen
from scores import get_record
from display import score_display
from scores import load

#Main function that contains the logic that ties all the files/funcs together:
def main():
    games_played = 0
    games_won = 0
    games_lost = 0
    while True:
        welcome_screen()
        choice = int(input("Please choose one of the options displayed in the welcome screen (1-4): "))
        if choice == 1:
            difficulty_display()
            diff_choice = int(input("Please enter one of the difficulties mentioned above (1-3): "))
            if diff_choice == 1:
                difficulty_chosen = difficulty["easy"]
                difficulty_name = "easy"
            elif diff_choice == 2:
                difficulty_chosen = difficulty["medium"]
                difficulty_name = "medium"
            elif diff_choice == 3:
                difficulty_chosen = difficulty["hard"]
                difficulty_name = "hard"
            else:
                print("You have not inputed a correct difficulty (1-3): ")
                continue
            result = core_loop(difficulty_chosen, difficulty_name)
            if result == True:
                games_won += 1
                games_played += 1
            else:
                games_lost += 1
                games_played += 1
        elif choice == 2:
            print(get_record("easy"))
            print(get_record("medium"))
            print(get_record("hard"))
        elif choice == 3:
            scores = load()
            for diff_name in ["easy", "medium", "hard"]:
                score_display(scores[diff_name], diff_name)
        elif choice == 4:
            print(f"Games Played: {games_played}")
            print(f"Games Won: {games_won}")
            print(f"Games Lost: {games_lost}")
            break
        elif choice not in range(1,5):
            print("You have not chosen a supported option (1-4)")

#If condition that executes the main function:
if __name__ == "__main__":
    main()