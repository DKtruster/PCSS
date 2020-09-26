import tkinter as tk
from tkinter import *
import threading
from PIL import Image, ImageTk

w = tk.Tk()
w.title("Game_name")
w.geometry("1200x700")

bg1 = Image.open("backgroundBoard.jpg")
bgPT = ImageTk.PhotoImage(bg1)
label = Label(image=bgPT)

textBut = Image.open("testButtonTexture.jpg")
textButPT = ImageTk.PhotoImage(textBut)
textButPTL = Label(image=textButPT)

runCheck = False


class displayGUI():
    # GUI Set-up made with help from: https://www.geeksforgeeks.org/python-gui-tkinter/
    def __init__(self, runcheck: bool):
        runCheck = runcheck

        for i in range(10):
            stringHolder = "cardHolder" + str(i)
            stringHolder = tk.Button(w, width=15, height=10, text=("Card " + str(i)))
            stringHolder.config(bg='lightgreen')

            if i < 5:
                stringHolder.place(relx=1, x=-80 - (i * 120), y=100, anchor=NE)
            if i >= 5:
                stringHolder.place(relx=1, x=-80 - ((i - 5) * 120), y=350, anchor=NE)

        for i in range(5):
            stringHolder = "Shop card " + str(i)
            stringHolder = tk.Button(w, width=35, height=5, text=("Card " + str(i)))
            stringHolder.config(bg='lightgreen')

            stringHolder.place(relx=1, x=-1110, y=120+(i * 90), anchor=NW)

        sceneUpdateButton = tk.Button(w, width=250, height=50, image = textButPT, compound=LEFT)
        sceneUpdateButton.place(relx=1, x=-500, y=620, anchor=NE)

        label.grid(row=0,column=0)
        w.mainloop()
        # threading.Thread.__init__(target=w.mainloop()).start
