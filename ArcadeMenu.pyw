#!/usr/bin/env python3
from threading import Thread
import sys

import tkinter as tk
from tkinter import font
from tkinter import *

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
        pass


    if yesno == True:


        # Window config:
        window = tk.Tk()
        # if fullscreen equals to false, start the window in resolutions:
        # 1366x768
        # goofy resolution am i right? that's the arcade screen's resolution.
        if fullscreen == False:
            window.geometry('1366x768')
            window.configure(bg='#1C1D1F', cursor="none")
            window.attributes("-fullscreen", False)
        # if fullscreen is true (which is the default)
        # start in fullscreen
        if fullscreen == True:
            window.geometry('1366x768')
            window.configure(bg='#1C1D1F', cursor="none")
            window.attributes("-fullscreen", True)

        window.title("ArcadeMenu")

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
            window.configure(bg='#1C1D1F', cursor="none")
            window.attributes("-fullscreen", False)
        # if fullscreen is true (which is the default)
        # start in fullscreen
        if fullscreen == True:
            window.configure(bg='#1C1D1F', cursor="none")
            window.attributes("-fullscreen", True)

        window.title("ArcadeMenu")

        main()

        window.mainloop()







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
