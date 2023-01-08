import os

working_dir = os.getcwd()

def getNumberOfGames():
    arcademenudir = working_dir[8:]
    gameslistdir = arcademenudir + "/gameslist/games.txt"

    with open(gameslistdir,"r") as f:
        for line in f:
            #do something here




getNumberOfGames()

print("No Command Specified")
print("Or, if you want to know the commands, then sure! here:\n")
print("There are currently no commands xD")
input()