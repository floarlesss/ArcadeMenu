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
    exit()


def startwithlogo(arg):
    if arg == True:
        # Window config:
        window = tk.Tk()
        window.geometry('900x500')
        window.configure(bg='#1C1D1F', cursor="none")
        #window.attributes("-fullscreen", True)
        window.title("ArcadeMenu")

        logo_img = tk.PhotoImage(file="icons_and_logo/logo/logo_full/logo_fullscreen.png")
        logo_imgLabel = tk.Label(window, image = logo_img)
        logo_imgLabel.pack(fill=BOTH, expand=True)
        


        window.mainloop()






# Count the arguments
arguments = len(sys.argv) - 1
# If there is more than one argument, it tells the user and proceeds
# to call the "printhelp" function.
if arguments > 1:
    print("Sorry, this program only accepts one argument.")
    printhelp()
elif arguments == 0:
    print("No arguments were provided.")
    printhelp()
else:
    # Output argument-wise
    # Dev note: Okay.. this looks complicated. Here's some comments to
    # help you understand this.

    # A position variable is made, so the code can loop through more than
    # one argument if that capability is added later.
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
                argument = argument[14:]
                # (this would make the argument variable "false" or "true"
                # depending on what the user input.)

                # Having ".lower()" makes it so that the program is
                # capable of being case-insensitive. So you can
                # literally just pass this argument: 
                # "--startwithlogo=FaLSe" and it would accept it.

                # If the argument is "false", call the startwithlogo
                # functions with an argument: "False". I would of explained
                # this in the "startwithlogo" function.
                if argument.lower() == "false":
                    startwithlogo(False)

                if argument.lower() == "true":
                    startwithlogo(True)

            # If the argument doesn't start with "startwithlogo",
            # Tell the user and call the "printhelp" function. 
            if argument.startswith("startwithlogo") == False:
                print("That argument is not recognised.")
                printhelp()
        # If the argument doesn't start with "--", it prints a notice
        # to the user that it's not recognised, and calls the printhelp
        # function.
        else:
            print("That argument is not recognised.")
            printhelp()
        position = position + 1