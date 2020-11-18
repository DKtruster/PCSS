import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import random
import cards
import Assets
import serverClient
import time
import threading

# WINDOW SETUP
window = tk.Tk()
window.title("PCSS Project - Lukas Kristensen")
window.geometry("1200x700")
window.resizable(False, False)

cardObjects, playerCards, shopCards, boardArray, shopArray = [], [], [], ["", "", "", "", "", "", "", "", "", ""], ["", "", "", "", ""]

for x in range(len(Assets.cardImg)):
    Assets.cardImg[x] = ImageTk.PhotoImage(Assets.cardImg[x])

for x in range(len(Assets.shopImg)):
    Assets.shopImg[x] = ImageTk.PhotoImage(Assets.shopImg[x])

cardImgLen = len(Assets.cardImg)-1

# LOADING IMAGES
bgPT = ImageTk.PhotoImage(Assets.bg1)
backgroundL = Label(image=bgPT)

textBut = Image.open("Assets/testButtonTexture.jpg")
textButPT = ImageTk.PhotoImage(textBut)

CDunknown = Image.open("Assets/unknown1low.jpg")
CDunknownPT = ImageTk.PhotoImage(CDunknown)

runCheck = False

def moveCard():
    for i in range (11):
        playerCards[0].place(y = 350-(i*8))
        time.sleep(0.0001)
    for i in range (11):
        playerCards[0].place(y = 270+(i*8))
        time.sleep(0.0001)

def shopBuy(shopNumber):
    cardPlaceStrHold = ""
    if len(cardObjects) < 5:
        for i in range(cardImgLen+1):
            if shopArray[shopNumber] == i:
                for c in range(5):
                    if (boardArray[c] == ""):
                        cardPlaceStrHold = "cardPlace" + str(c)
                        cardPlaceStrHold = cards.Cards()
                        print("Searching data for:",i)
                        cardPlaceStrHold.searchData(str(i))
                        playerCards[c].configure(image=Assets.cardImg[i])
                        playerCards[c].configure(text="\n\n\n\n\n\n\n\n\n\n\n" + str(cardPlaceStrHold.get_damage()) + "                " + str(cardPlaceStrHold.get_health()))
                        boardArray[c] = i
                        # boardArray[c] = cardPlaceStrHold.get_name()
                        if len(cardObjects) > c:
                            cardObjects[c] = cardPlaceStrHold
                        cardObjects.append(cardPlaceStrHold)
                        print("System message: Purchased: " + str(cardPlaceStrHold.get_name()))
                        return
            if i == 2:
                print("System message: No more capacity")


def shopRandom():
    for i in range(5):
        rand = random.randint(0, cardImgLen)
        shopCards[i].configure(image=Assets.shopImg[rand])
        shopArray[i] = rand
    if len(cardObjects) > 0:
        displayGUI.updateCards(self="")
        displayGUI(True)

def endRound():
    threadSend = threading.Thread(target=moveCard)
    threadSend.start()
    while len(cardObjects)<5:
        rand = random.randint(0, cardImgLen)
        shopBuy(rand)

    if len(cardObjects)<6:
        for c in range(5):
            rand = random.randint(0, cardImgLen)
            if (boardArray[c+5] == ""):
                cardPlaceStrHold = "cardPlace" + str(c)
                cardPlaceStrHold = cards.Cards()
                cardPlaceStrHold.searchData(str(rand))
                playerCards[c+5].configure(image=Assets.cardImg[rand])
                playerCards[c+5].configure(
                    text="\n\n\n\n\n\n\n\n\n\n\n" + cardPlaceStrHold.get_damage() + "                " + cardPlaceStrHold.get_health())
                boardArray[c+5] = cardPlaceStrHold.get_name()
                if len(cardObjects) > c+5:
                    cardObjects[c+5] = cardPlaceStrHold
                cardObjects.append(cardPlaceStrHold)
                print("System message: Enemy Purchased: " + str(cardPlaceStrHold.get_name()))
    displayGUI.updateCards("")

    serverClient.clientServerReceive()
    # serverClient.clientServerSend()
    serverClient.serverSend(boardArray)

def cardSelect(PlayerSelect, cardNumber):
    if len(cardObjects) < 6:
        boardArray[cardNumber] = ""
        playerCards[cardNumber].configure(image=CDunknownPT, text="")
        displayGUI.updateCards(self="")

        print("Card: " + str(cardNumber) + " Player: " + str(PlayerSelect))
        print(boardArray[0] + " " + boardArray[1] + " " + boardArray[2] + " " + boardArray[3] + " " +
              boardArray[4])
        print(boardArray[5] + " " + boardArray[6] + " " + boardArray[7] + " " + boardArray[8] + " " +
              boardArray[9])
    if len(cardObjects) > 5:
        print("System message: Can't make any board changes while the game is running")



class displayGUI():
    # GUI Set-up made with help from: https://www.geeksforgeeks.org/python-gui-tkinter/
    def __init__(self, runcheck: bool):

        for i in range(10):
            if i < 5:
                playerCards[i].place(relx=1, x=-720 - ((i - 5) * 120), y=350, anchor=NE)
            if i >= 5:
                playerCards[i].place(relx=1, x=480 - (i * 120), y=100, anchor=NE)

        for i in range(5):
            shopCards[i].place(relx=1, x=-1150, y=110 + (i * 95), anchor=NW)

        sceneUpdateButton = tk.Button(window, width=250, height=50, image=textButPT, compound=LEFT, command=endRound)
        sceneUpdateButton.place(relx=1, x=-500, y=620, anchor=NE)

        backgroundL.grid(row=0, column=0)
        window.mainloop()

    def updateCards(self):
        for i in range(10):
            if int(cardObjects[i].get_health())<1:
                boardArray[i]=""

            if boardArray[i] != "":
                playerCards[i].configure(text="\n\n\n\n\n\n\n\n\n\n\n" + str(cardObjects[i].get_damage()) + "                " + str(cardObjects[i].get_health()))
            if boardArray[i] == "":
                playerCards[i].configure(text="", image=CDunknownPT)

    def setup(self):
        for i in range(10):
            stringHolder = "cardHolder" + str(i)

            if i < 5:
                stringHolder = tk.Button(window, width=105, height=185, image=CDunknownPT, fg="white", compound=tk.CENTER, command=lambda holder=i: cardSelect(1, holder))
                playerCards.append(stringHolder)
            else:
                stringHolder = tk.Button(window, width=105, height=185, image=CDunknownPT, fg="white", compound=tk.CENTER, command=lambda holder=i: cardSelect(2, holder))
                playerCards.append(stringHolder)

        for i in range(5):
            stringHolder = "ShopCard" + str(i)
            stringHolder = tk.Button(window, width=290, height=95, command=lambda holder=i: shopBuy(holder))
            shopCards.append(stringHolder)
        shopRandom()
