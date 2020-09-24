import tkinter as tk
from tkinter import *

class displayGUI():
    # GUI Set-up made with help from: https://www.geeksforgeeks.org/python-gui-tkinter/
    w = tk.Tk()
    w.title("Game_name")
    w.geometry("1200x700")


    for i in range(10):
        stringHolder = "cardHolder" + str(i)
        stringHolder = tk.Button(w, width=15, height=10, text=("Card " + str(i)))
        stringHolder.config(bg='lightgreen')

        if (i < 5):
            stringHolder.place(relx=1, x=-50 - (i * 120), y=100, anchor=NE)
        if (i >= 5):
            stringHolder.place(relx=1, x=-50 - ((i - 5) * 120), y=350, anchor=NE)


    sceneUpdateButton = tk.Button(w, text='Update scene', width=15, height=10)
    sceneUpdateButton.place(relx=1, x=-1000, y=150, anchor=NE)

    w.mainloop()