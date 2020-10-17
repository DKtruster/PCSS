from gui import displayGUI
import cards
import threading

class main:
    # SETUP

    cards.sortCards()
    displayGUI.setup("")
    displayGUI(True)


