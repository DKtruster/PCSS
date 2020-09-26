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
                stringHolder.place(relx=1, x=-50 - (i * 120), y=100, anchor=NE)
            if i >= 5:
                stringHolder.place(relx=1, x=-50 - ((i - 5) * 120), y=350, anchor=NE)

        sceneUpdateButton = tk.Button(w, text='Update scene', width=15, height=10)
        sceneUpdateButton.place(relx=1, x=-1000, y=150, anchor=NE)

        label.grid(row=0,column=0)

        w.mainloop()
        # threading.Thread.__init__(target=w.mainloop()).start
