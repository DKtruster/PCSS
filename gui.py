import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# WINDOW SETUP
window = tk.Tk()
window.title("PCSS Project - Lukas")
window.geometry("1200x700")

playerCards, shopCards = [],[]

# LOADING IMAGES
bg1 = Image.open("Assets/backgroundBoard3.jpg")
bgPT = ImageTk.PhotoImage(bg1)
backgroundL = Label(image=bgPT)

textBut = Image.open("Assets/testButtonTexture.jpg")
textButPT = ImageTk.PhotoImage(textBut)

CDviking1 = Image.open("Assets/viking1low.jpg")
CDviking1PT = ImageTk.PhotoImage(CDviking1)

SPviking1 = Image.open("Assets/viking1shop.jpg")
SPviking1PT = ImageTk.PhotoImage(SPviking1)

CDunknown = Image.open("Assets/unknown1low.jpg")
CDunknownPT = ImageTk.PhotoImage(CDunknown)

runCheck = False


def shopBuy(cardNumber):
    playerCards[5].configure(image=CDviking1PT)
    print("Shop: " + str(cardNumber))


def cardSelect(PlayerSelect, cardNumber):
    playerCards[cardNumber].configure(image=CDunknownPT)
    print("Card: " + str(cardNumber) + " Player: " + str(PlayerSelect))


class displayGUI():
    # GUI Set-up made with help from: https://www.geeksforgeeks.org/python-gui-tkinter/
    def __init__(self, runcheck: bool):
        runCheck = runcheck

        for i in range(10):
            if i < 5:
                playerCards[i].place(relx=1, x=-80 - (i * 120), y=100, anchor=NE)
            if i >= 5:
                playerCards[i].place(relx=1, x=-80 - ((i - 5) * 120), y=350, anchor=NE)

        for i in range(5):
            shopCards[i].place(relx=1, x=-1150, y=110 + (i * 95), anchor=NW)

        sceneUpdateButton = tk.Button(window, width=250, height=50, image=textButPT, compound=LEFT)
        sceneUpdateButton.place(relx=1, x=-500, y=620, anchor=NE)

        backgroundL.grid(row=0, column=0)
        window.mainloop()
        # threading.Thread.__init__(target=w.mainloop()).start

    def setup(self):
        for i in range(10):
            stringHolder = "cardHolder" + str(i)

            if i < 5:
                stringHolder = tk.Button(window, width=105, height=185, image=CDunknownPT, compound=LEFT,
                                         command=lambda holder=i: cardSelect(1, holder))
                playerCards.append(stringHolder)
            else:
                stringHolder = tk.Button(window, width=105, height=185, image=CDunknownPT, compound=LEFT,
                                         command=lambda holder=i: cardSelect(2, holder))
                playerCards.append(stringHolder)

        for i in range(5):
            stringHolder = "ShopCard" + str(i)
            stringHolder = tk.Button(window, width=290, height=95, image=SPviking1PT,command=lambda holder=i: shopBuy(holder))
            shopCards.append(stringHolder)
