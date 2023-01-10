import os

working_dir = os.getcwd()

def getNumberOfGames():
    # declare number of games function variables:
    number_of_games = 0
    newgame = False


    arcademenudir = working_dir[:-8]
    gameslistdir = arcademenudir + "\\gameslist\\games.txt"

    # Open the games list .txt file
    with open(gameslistdir,"r") as f:
        # Loop through all the lines in the file
        for line in f:
            global ln

             # If the line starts with "NEW GAME:"
            if line.startswith("NEW GAME:"):
                newgame = True
                ln = 0
            else:
                print("No games were detected.")
                print("Maybe \"NEW GAME\" isn't added in the games.txt file?")
                return "NoGamesDetected"

            # Counting over function, this is called when the string
            # "END OF LIST"
            def countingover(finished_number_of_games):
                global newgame, number_of_games
                print("Counting over.")
                print("Number of games:\n"+ str(finished_number_of_games) +"")

                newgame = False
                number_of_games = 0
                return number_of_games


            if line == "END OF LIST":
                countingover(number_of_games)

            # If the line starts with "#", pass (because it's a comment)
            if line.startswith("#"):
                print("line has #")
                pass
            # If newgame is equal to true, count the lines until it's
            if newgame == True:
                # If the ln variable is 4 (the number of line a game
                # should be in the gameslist), add one to the number of
                # games.
                if ln == 4:
                    number_of_games += 1
                    newgame = False
                # If the line is comment (starts with "#"), do nothing.
                if line.startswith("#"):
                    pass
                # Else, add one to the line count.
                else:
                    ln += 1


            else: 
                pass



print("Hey! It seems you've run this file from the terminal.")
print("You can use this file from the terminal if you plan to debug it.\n")
print("1) Count number of games\n")
print("Enter 1")

command = int(input(""))
print()

if command != 1:
    print("Sorry, that's not a command.")


if command == 1:
    getNumberOfGames()