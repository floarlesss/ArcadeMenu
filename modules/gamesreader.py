import os

working_dir = os.getcwd()

def getNumberOfGames():
    global number_of_games
    number_of_games = 0

    arcademenudir = working_dir[:-8]
    gameslistdir = arcademenudir + "\\gameslist\\games.txt"

    # Open the games list .txt file
    with open(gameslistdir,"r") as f:
        # Loop through all the lines in the file
        for line in f:
            global newgame, ln
            # If the line starts with "#", pass (because it's a comment)
            if line.startswith("#"):
                pass
            # If newgame is equal to true, count the lines until it's
            if newgame == True:
                # If the ln variable is 4 (the number of line a game
                # should be in the gameslist), add one to the number of
                # games.
                if ln == 4:
                    number_of_games += 1
                # If the line is comment (starts with "#"), do nothing.
                if line.startswith("#"):
                    pass
                # Else, add one to the line count.
                else:
                    ln += 1


            else: 
                pass

            # If the line starts with "NEW GAME:"
            if line.startswith("NEW GAME:"):
                newgame = True
                ln = 0




getNumberOfGames()

print("No Command Specified")
print("Or, if you want to know the commands, then sure! here:\n")
print("There are currently no commands xD")