#!/usr/bin/env python3
from threading import Thread

import tkinter as tk
from tkinter import font
from tkinter import *

window = tk.Tk()
window.geometry('900x500')
window.configure(bg='#1C1D1F', cursor="none")
window.attributes("-fullscreen", True)
window.title("ArcadeMenu")

frameCnt = 30
frames = [PhotoImage(file="icons_and_animations/startup/startupgif.gif",format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame, bg='#1C1D1F')
    window.after(30, update, ind)
label = Label(window)
label.place(relx=.5, rely=.5, anchor= CENTER)