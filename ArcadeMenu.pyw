#!/usr/bin/env python3
import readFile
from threading import Thread
import sys
from configparser import ConfigParser
import PIL
from PIL import Image as PILimage

import tkinter as tk
from tkinter import messagebox
from tkinter import *

# Read the configurations file
configFilePath = "admin/settings.ini"

config = ConfigParser()
config.read(configFilePath)


autodetectSetting = config["autoDetectIcons"]["autodetection"]

ableJoysticks = config["gameSelectors"]["ableJoysticks"]
joystickAbleToSelect = config["gameSelectors"]["joystickAbleToSelect"]


# The "printhelp" function is just a simple function that prints the
# command(s) that you can pass into the program.
# This is called when the program doesn't recognise a command or none are
# passed into it.
def printhelp():
    print("\nArguments:")
    print('--startwithlogo\nYou can pass "true" or "false" into this. (case-insensitive)')
    print("Here's an example: python ArcadeMenu.pyw --startwithlogo=true")
    print("This argument is mandatory.\n")

    print("There is a fullscreen argument, which allows you to change if the program starts in fullscreen or not.")
    print("If you pass false into this argument, it will start in the resolution: 1366x768")

    print("You can pass two arguments. Like this:")
    print("python ArcadeMenu.pyw --startwithlogo=true --fullscreen=false")
    print("Please note that the fullscreen argument is not mandatory.")
    exit()


def startwithlogo(yesno, fullscreen=True):
    # globalise some variables so they can be used later in functions
    global window

    def main():
        def gameinfohandler(firstTimeRan = True, listOfGames = [], obj = None, listnum = 0):
            if firstTimeRan == True:
                return readFile.getGames()
            
            else:
                if obj == "name":
                    currentGame = listOfGames[listnum]
                    return currentGame.name
                if obj == "description":
                    currentGame = listOfGames[listnum]
                    return currentGame.description
                if obj == "images":
                    currentGame = listOfGames[listnum]
                    return currentGame.images
                if obj == "author":
                    currentGame = listOfGames[listnum]
                    return currentGame.author
                if obj == "executable":
                    currentGame = listOfGames[listnum]
                    return currentGame.executable

        global currentgame, maxgamenum
        currentgame = 1
        maxgamenum = len(gameinfohandler())

        def gameselectorhandler(direction = None):
            # This is an example for me to use and add on later in
            # developing ArcadeMenu.
            #game_frame_nameLabel[2]["text"] = "hi dis is test text lel"


            global currentgame, maxgamenum
            print(str(currentgame))

            for i in range(len(gameinfohandler())):
                if i == 0:
                    pass
                else:
                    print()
                    #game_frame[i]['bg'] = '#2E2E2E'



            if direction == "up":
                    print("up")
                    currentgame -= 1
                    #game_frame[currentgame]['bg'] = '#525252'

            if direction == "down":
                    print("down")
                    currentgame += 1
                    #game_frame[currentgame]['bg'] = '#525252'
                    


            gameselectorhandler()
            # Selector keybinds
            if ableJoysticks == "both":
                # If ableJoysticks (set in the settings.ini file)
                # is set to "both", bind both p1 and p2 keybinds to
                # the gameselectorhandler function.

                # Player 1 binds
                window.bind("w", lambda e: gameselectorhandler("up"))
                window.bind("s", lambda e: gameselectorhandler("down"))

                # Player 2 binds
                window.bind("i", lambda e: gameselectorhandler("up"))
                window.bind("k", lambda e: gameselectorhandler("down"))
            if ableJoysticks == "mono":
                # If ableJoysticks (set in the settings.ini file)
                # is set to "mono", the joystickAbleToSelect config
                # will be read and if it's set to "left" the keybinds
                # are set.

                # Same goes for if the setting is set to "right"
                if joystickAbleToSelect == "left":
                    # Player 1 binds
                    window.bind("w", lambda e: gameselectorhandler("up"))
                    window.bind("s", lambda e: gameselectorhandler("down"))


                if joystickAbleToSelect == "right":
                    # Player 2 binds
                    window.bind("i", lambda e: gameselectorhandler("up"))
                    window.bind("k", lambda e: gameselectorhandler("down"))


            


        def main():
            listOfGames = gameinfohandler()
            #creategameoptions(listOfGames)

        main()




    if yesno == True:
        # Window config:
        window = tk.Tk()
        # if fullscreen equals to false, start the window in resolutions:
        # 1366x768
        # goofy resolution am i right? that's the arcade screen's resolution.
        if fullscreen == False:
            window.geometry('1366x768')
        # if fullscreen is true (which is the default)
        # start in fullscreen
        if fullscreen == True:
            screenWidth = window.winfo_screenwidth()
            screenHeight = window.winfo_screenheight()

            window.overrideredirect(True)
            window.geometry('+0+0')
            window.geometry('900x500')

            window.geometry(""+ str(screenWidth) +"x"+ str(screenHeight) +"")

        window.configure(bg='#292929', cursor="none")
        window.resizable(False, False)
        window.title("ArcadeMenu")

        try:
            with open("icons_and_logo/logo/logo_full/logo_custom.png", "r"):
                pass
        except FileNotFoundError:
            image = PILimage.open('icons_and_logo/logo/logo_full/logo_fullscreen.png')
            image.thumbnail((screenWidth, screenHeight), PILimage.ANTIALIAS)
            image.save('icons_and_logo/logo/logo_full/logo_custom.png', 'PNG', quality=300)
        except Exception as e:
            messagebox.showerror("Error loading file", str(e))

        # load the logo image to pack (place) onto screen later
        logoFullscreen_img = tk.PhotoImage(file="icons_and_logo/logo/logo_full/logo_fullscreen.png")
        logo_panel = tk.Label(window, image = logoFullscreen_img)
        logo_panel.pack(fill=BOTH, expand=True)
        # ^ this is where it packs the logo panel to the screen. above it is configuring
        # it before the widget is packed.

        def destroyImageAndCallMain():
            logo_panel.destroy()
            main()

        window.after(1500, destroyImageAndCallMain)


        window.mainloop()
    

    if yesno == False:
        # Window config:
        window = tk.Tk()
        # if fullscreen equals to false, start the window in resolutions:
        # 1366x768
        # goofy resolution am i right? that's the arcade screen's resolution.
        if fullscreen == False:
            window.geometry('1366x768')
            window.attributes("-fullscreen", False)
        # if fullscreen is true (which is the default)
        # start in fullscreen
        if fullscreen == True:
            screenWidth = window.winfo_screenwidth()
            screenHeight = window.winfo_screenheight()

            window.overrideredirect(True)
            window.geometry('+0+0')
            window.geometry('900x500')

            window.geometry(""+ str(screenWidth) +"x"+ str(screenHeight) +"")

        window.configure(bg='#1C1D1F', cursor="none")
        window.title("ArcadeMenu")

        main()

        window.mainloop()





def handleargs():
    # THIS IS THE ARGUMENT PART OF THE PROGRAM
    # When you start the program, this is what handles the arguments.

    # Count the arguments
    arguments = len(sys.argv) - 1
    # If there is more than one argument, it tells the user and proceeds
    # to call the "printhelp" function.
    if arguments > 2:
        print("Sorry, this program only accepts two arguments.")
        printhelp()
    elif arguments == 0:
        print("No arguments were provided.")
        printhelp()
    else:
        # Output argument-wise
        # Dev note: Okay.. this looks complicated. Here's some comments to
        # help you understand this.

        # A position variable is made, so the code can loop through more than
        # one argument.
        position = 1

        # This while loop is added so the code can loop through more than one
        # argument.
        while (arguments >= position):
            # If the argument starts with "--", it will slice the argument by 2
            # from the start. So "--test" would become "test".
            if (sys.argv[position]).startswith("--"):
                # This is where the argument is sliced.
                argument = (sys.argv[position])[2:]
                # Here, we have to do a ".startswith()" because sys.argv
                # intakes "--test=false" as one argument.
                if argument.startswith("startwithlogo"):
                    # The argument is sliced by 14, which is the length of
                    # "startwithlogo" (< is from a sliced variable above.)
                    argument1 = argument[14:]
                    # (this would make the argument variable "false" or "true"
                    # depending on what the user input.)


                    # Having ".lower()" makes it so that the program is
                    # capable of being case-insensitive. So you can
                    # literally just pass this argument: 
                    # "--startwithlogo=FaLSe" and it would accept it.

                    # If the argument is "false", call the startwithlogo
                    # functions with an argument: "False". I would of explained
                    # this in the "startwithlogo" function.
                    if argument1.lower() == "false":
                        swlArg = False

                    if argument1.lower() == "true":
                        swlArg = True

                # If the argument doesn't start with "startwithlogo",
                # Tell the user and call the "printhelp" function. 
                if argument.startswith("fullscreen"):
                    # The same happens as last time, we slice the argument so the string
                    # "fullscreen=true" turns to "true".
                    argument2 = sys.argv[2]
                    argument2 = argument[11:]

                    if argument2.lower() == "false":
                        fullscreenArg = False
                    if argument2.lower() == "true":
                        fullscreenArg = True
                    
            # If the argument doesn't start with "--", it prints a notice
            # to the user that it's not recognised, and calls the printhelp
            # function.
            else:
                print("That argument is not recognised.")
                printhelp()
            position = position + 1


    # This is the final bit of code, starts everything... kinda like a "launch!" system
    if arguments == 2:
        if swlArg == True and fullscreenArg == True:
            startwithlogo(True)
        if swlArg == False and fullscreenArg == True:
            startwithlogo(False)

        if swlArg == True and fullscreenArg == False:
            startwithlogo(True, False)
        if swlArg == False and fullscreenArg == False:
            startwithlogo(False, False)
    if arguments == 1:
        if swlArg == True:
            startwithlogo(True)
        if swlArg == False:
            startwithlogo(False)

handleargs()