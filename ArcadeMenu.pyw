#!/usr/bin/env python3
import readFile
from threading import Thread
import sys
from configparser import ConfigParser
from PIL import Image as PILimage

import tkinter as tk
from tkinter import messagebox
from tkinter import *

print("LOGS:\n")


# Loading function, this function is ran immediately when the program is started so it can load things like images.
def load():
    print("\nLoading...\n")
    # This is where you can load images, gifs, videos or anything that takes time
    # to load.
    print("\nLoading finished.\n")


print("CONFIG CODE:")
print(" Reading config file...")

try:
    # Read the configurations file
    print("Setting the config file path variable")
    configFilePath = ".PROGRAM_FILES/admin/settings.ini"

    print("Initializing config parser")
    config = ConfigParser()
    print("Reading config file")
    config.read(configFilePath)

    print("Setting autodetect setting variable...\n")
    autodetectSetting = config["autoDetectIcons"]["autodetection"]

    ableJoysticks = config["gameSelectors"]["ableJoysticks"]
    joystickAbleToSelect = config["gameSelectors"]["joystickAbleToSelect"]
except Exception as e:
    print("There was an error during the configuration part of the program. Error info:\n"+ str(e) +"")
    try:
        window.destroy()
    except:
        pass
    messagebox.showerror("Error during config setup",
    "An error occured whilst trying to setup the configuration values. Error info:\n"+ str(e) +"")
    exit()
else:
    print("CONFIG CODE FINISHED")


# The "exit_program" function is a function that is called when
# "x" is pressed. This feature is added because it is very hard
# to try and exit ArcadeMenu in fullscreen mode.
def exit_program(window):
    window.destroy()
    exit(0)


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


def program(yesno, fullscreen=True):
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


            

        def graphical_elements():
            print("\nMAIN STARTED\n")

            



            def config_widgets():
                global screenWidth, split_frame
                screenWidth = window.winfo_screenwidth()

                split_frame = tk.Frame(window, bg='#595959', height=50, width=25)

                def left_side():
                    global left_frame
                    # This is the left side of the GUI (split by the "split_frame" frame).
                    left_frame = tk.Frame(window, bg='#1C1D1F', height=50, width=screenWidth / 2 - 25)
                def right_side():
                    global right_frame
                    # THis is the right side of the GUI (split by the "split_frame" frame).
                    right_frame = tk.Frame(window, bg='#1C1D1F', height=50, width=screenWidth / 2)

                # This is the part of the program where the widgets are given variables and configurations.

                left_side()
                right_side()


            def pack():
                # This is the part of the program where all of the widgets are packed onto the screen.
                def framePack():
                    window.rowconfigure(0, weight=1)

                    left_frame.grid(row=0, column=1, sticky="nsew")
                    split_frame.grid(row=0, column=2, sticky="nsew")
                    right_frame.grid(row=0, column=3, sticky="nsew")

                    




                config_widgets()
                framePack()


            config_widgets()  
            pack()

            listOfGames = gameinfohandler()
            #creategameoptions(listOfGames)

        graphical_elements()


    
    def startwindow():
        def start():
            global window

            def resizeImg(mode):
                try:
                    with open(".PROGRAM_FILES/icons_and_logo/logo/logo_full/logo_custom.png"):
                        pass
                except FileNotFoundError:
                    screenWidth = window.winfo_screenwidth()
                    screenHeight = window.winfo_screenheight()

                    if mode == "windowed":
                        image = PILimage.open('.PROGRAM_FILES/icons_and_logo/logo/logo_full/logo_fullscreen.png')
                    if mode == "fullscreen":
                        image = PILimage.open('.PROGRAM_FILES/icons_and_logo/logo/logo_full/logo_large.png')

                    resized_image = image.resize((screenWidth, screenHeight))
                    resized_image.save('.PROGRAM_FILES/icons_and_logo/logo/logo_full/logo_custom.png', 'PNG', quality=300)
                    return 2

                except Exception as e:
                    messagebox.showerror("Error loading file", str(e))
                    return 0
                else:
                    screenWidth = window.winfo_screenwidth()
                    screenHeight = window.winfo_screenheight()

                    custom_image = PILimage.open('.PROGRAM_FILES/icons_and_logo/logo/logo_full/logo_custom.png')
                    if custom_image.width != screenWidth and custom_image.height != screenHeight:
                        resized_image = image.resize((screenWidth, screenHeight))
                        resized_image.save('.PROGRAM_FILES/icons_and_logo/logo/logo_full/logo_custom.png', 'PNG', quality=300)
                        return 3
                    else:
                        return 1

            if yesno == True:
                # Window config:
                window = tk.Tk()
                # if fullscreen equals to false, start the window in resolutions:
                # 1366x768
                # goofy resolution am i right? that's the arcade screen's resolution.
                if fullscreen == False:
                    window.geometry('1366x768')
                    window.resizable(False, False)
                    bindExitButton(window)
                # if fullscreen is true (which is the default)
                # start in fullscreen
                if fullscreen == True:
                    window.attributes("-fullscreen", True)
                    bindExitButton(window)

                window.configure(bg='#292929', cursor="none")
                window.title("ArcadeMenu")

                # Resizing the logo image so it fits on any screen.
                if fullscreen == True:
                    resizeResult = resizeImg("fullscreen")
                if fullscreen == False:
                    resizeResult = resizeImg("windowed")

                if resizeResult == 1 or resizeResult == 2 or resizeResult == 3:
                    def destroyImageAndCallMain():
                        logo_panel.destroy()
                        main()
                    window.after(1500, destroyImageAndCallMain)
                if resizeResult == 0:
                    window.destroy()
                    exit()

                # load the logo image to pack (place) onto screen later
                if fullscreen == True:
                    logoFullscreen_img = tk.PhotoImage(file=".PROGRAM_FILES/icons_and_logo/logo/logo_full/logo_custom.png")
                if fullscreen == False:
                    logoFullscreen_img = tk.PhotoImage(file=".PROGRAM_FILES/icons_and_logo/logo/logo_full/logo_fullscreen.png")

                logo_panel = tk.Label(window, image = logoFullscreen_img)
                logo_panel.pack(fill=BOTH, expand=True)
                # ^ this is where it packs the logo panel to the screen. above it is configuring
                # it before the widget is packed.


                window.mainloop()
            

            if yesno == False:
                # Window config:
                window = tk.Tk()
                # if fullscreen equals to false, start the window in resolutions:
                # 1366x768
                # goofy resolution am i right? that's the arcade screen's resolution.
                if fullscreen == False:
                    window.geometry('1366x768')
                    window.resizable(False, False)
                    bindExitButton(window)
                # if fullscreen is true (which is the default)
                # start in fullscreen
                if fullscreen == True:
                    window.attributes("-fullscreen", True)
                    bindExitButton(window)

                window.configure(bg='#292929', cursor="none")
                window.title("ArcadeMenu")

                main()
                window.mainloop()

        def bindExitButton(window):
            # Bind the button X to the exit_program function
            window.bind("<BackSpace>", lambda e: exit_program(window))

        startThread = Thread(target=start)
        startThread.start()

    
    startwindow()



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
            program(True)
        if swlArg == False and fullscreenArg == True:
            program(False)

        if swlArg == True and fullscreenArg == False:
            program(True, False)
        if swlArg == False and fullscreenArg == False:
            program(False, False)
    if arguments == 1:
        if swlArg == True:
            program(True)
        if swlArg == False:
            program(False)


handleargs()

loadThread = Thread(target=load)
loadThread.start()