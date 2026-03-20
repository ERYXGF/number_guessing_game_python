"""Contains everything related to the high score system: loading scores from JSON, saving a new score, checking if a result is a new record, and retrieving the current record for a given difficulty."""

#Imports json to be able to load, save and access the json files:
import json

#Imports the path to the files i want to access:
from pathlib import Path

#Imports datetime to be able to save the new high scores date in the check_record function:
import datetime

#Defines what the path to scores.json is:
scores_path = Path("scores.json")

#Function that loads the users scores from the json file:
def load():
    #If the file doesn't exist or is empty:
    if not scores_path.exists() or scores_path.stat().st_size == 0:
        return("There are no scores saved yet.")
    with scores_path.open("r", encoding = "utf-8") as f:
        return json.load(f)
    
#Function that saves a new score:
def save(score):
    #Saves the scores to the file:
    with scores_path.open("w", encoding = "utf-8") as f:
        json.dump(score, f, indent = 4)

#Function that checks if the result is a new record:
def check_record(score, difficulty):
    #Loads all the scores that are in the file:
    scores = load()
    #Defines what scores that have the correct difficulty: 
    correct = scores[difficulty]
    #If correct is empty or > score:
    if correct == None or correct["best_attempts"] > score:
        print("Congratulations ! You just achieved a new record !")
        #Updates the file with the new record and its date:
        with scores_path.open("w", encoding = "utf-8") as f:
            scores[difficulty] = {"best_attempts" : score, "date" : str(datetime.date.today())}
            json.dump(scores, f, indent = 4)
        return True
    #If correct is < score:
    else:
        return False
    
#Function that gets the current high score:
def get_record(difficulty):
    #Loads all the scores that are in the file:
    scores = load()
    #Defines what scores have the wanted/correct difficulty:
    correct = scores[difficulty]
    #if there is no record:
    if correct == None:
        return ("There is no current record yet.")
    #If theres a record, load the record:
    else:
        return correct["best_attempts"]