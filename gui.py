import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

w = tk.Tk()
w.title("PCSS Project - Lukas")
w.geometry("1200x700")

bg1 = Image.open("backgroundBoard3.jpg")
bgPT = ImageTk.PhotoImage(bg1)
label = Label(image=bgPT)

textBut = Image.open("testButtonTexture.jpg")
textButPT = ImageTk.PhotoImage(textBut)

CDviking1 = Image.open("viking1low.jpg")
CDviking1PT = ImageTk.PhotoImage(CDviking1)

SPviking1 = Image.open("viking1shop.jpg")
SPviking1PT = ImageTk.PhotoImage(SPviking1)

CDunknown = Image.open("unknown1low.jpg")
CDunknownPT = ImageTk.PhotoImage(CDunknown)

runCheck = False



def shopBuy(cardNumber):
    print(cardNumber)

def cardSelect(PlayerSelect, cardNumber):
    print("Player Selected: #"+PlayerSelect+ "# Card Selected: #"+str(cardNumber)+"#")


class displayGUI():
    # GUI Set-up made with help from: https://www.geeksforgeeks.org/python-gui-tkinter/
    def __init__(self, runcheck: bool):
        runCheck = runcheck

        for i in range(10):
            stringHolder = "cardHolder" + str(i)

            if i < 5:
                stringHolder = tk.Button(w, width=105, height=185,image = CDunknownPT, compound=LEFT, command= lambda holder=i: cardSelect("Player1", holder))
            else:
                stringHolder = tk.Button(w, width=105, height=185,image = CDviking1PT, compound=LEFT, command= lambda holder=i: cardSelect("Player2",holder))

            if i < 5:
                stringHolder.place(relx=1, x=-80 - (i * 120), y=100, anchor=NE)
            if i >= 5:
                stringHolder.place(relx=1, x=-80 - ((i - 5) * 120), y=350, anchor=NE)


        for i in range(5):
            stringHolder = "ShopCard" + str(i)
            stringHolder = tk.Button(w, width=290, height=95,image = SPviking1PT, command= lambda holder="Shop"+str(i): shopBuy(holder))
            stringHolder.place(relx=1, x=-1150, y=110+(i * 95), anchor=NW)

        sceneUpdateButton = tk.Button(w, width=250, height=50, image = textButPT, compound=LEFT)
        sceneUpdateButton.place(relx=1, x=-500, y=620, anchor=NE)

        label.grid(row=0,column=0)
        w.mainloop()
        # threading.Thread.__init__(target=w.mainloop()).start
