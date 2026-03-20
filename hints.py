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
    
#Function that hints using the hot/cold proximity parameters:
def hot_cold(rand_num, guess, level):
    #Calculate the absolute difference between rand_num and guess:
    difference = abs(guess-rand_num)
    #Check if difference is in the first zone:
    if difference <= level["thresholds"][0][0]:
        return level["thresholds"][0][1]
    #Check if difference is in the second zone:
    elif difference <= level["thresholds"][1][0]:
        return level["thresholds"][1][1]
    #Check if difference is in the third zone:
    elif difference <= level["thresholds"][2][0]:
        return level["thresholds"][2][1]
    #Check if difference is in the fourth zone:
    elif difference <= level["thresholds"][3][0]:
        return level["thresholds"][3][1]
    #Check if difference is in neither zone:
    else:
        return ("Glacial")