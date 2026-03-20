"""Contains exclusively the hint functions. The higher/lower hint and the hot/cold proximity hint are separate functions here. 
Keeping them isolated makes them easy to modify without touching game logic."""

#Function that hints at whether the random num is higer or lower than the input:
def higher_lower(rand_num, guess):
    #Check if guess is higher than the correct value:
    if guess > rand_num:
        return("The random number is lower than your guess ")
    #Check if guess is lower than the correct value:
    elif guess < rand_num:
        return("The random number is higher than your guess ")
    #Check if the guess is equal to the correct value:
    else:
        return("Your guess was correct ! You won !")