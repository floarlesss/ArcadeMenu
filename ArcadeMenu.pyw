#!/usr/bin/env python3
from threading import Thread
import sys

import tkinter as tk
from tkinter import font
from tkinter import *

# Count the arguments
arguments = len(sys.argv) - 1
if arguments > 2:
    print("Sorry, this program only accepts two arguments.")
    exit()
else:
    # Output argument-wise
    position = 1
    while (arguments >= position):
        print((sys.argv[position]))
        position = position + 1

window = tk.Tk()
window.geometry('900x500')
window.configure(bg='#1C1D1F', cursor="none")
window.attributes("-fullscreen", True)
window.title("ArcadeMenu")


logo_image = PhotoImage(file="icons_and_logo/logo_full/logo_fullscreen.png")


window.mainloop()