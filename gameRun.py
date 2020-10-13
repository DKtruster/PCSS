import gui

class gameRun:
    def loadCombat(self, boardArray):
        playerOneCount = 0
        playerTwoCount = 0

        # Counts the amount of cards each player have
        for i in range(5):
            if boardArray[i] != "":
                playerOneCount = playerOneCount + 1

        for i in range(5):
            if boardArray[i + 5] != "":
                playerTwoCount = playerTwoCount + 1

        # Only starts the combat if one of the two players have a card on the deck
        if playerOneCount > 0 or playerTwoCount>0:
            print("Loading board...")
            print("PlayerOne has: "+str(playerOneCount)+ " cards \n PlayerTwo has: "+str(playerTwoCount)+" cards")
            print("PlayerOne: "+boardArray[0], boardArray[1], boardArray[2], boardArray[3], boardArray[4])
            print("PlayerTwo: "+boardArray[5], boardArray[6], boardArray[7], boardArray[8], boardArray[9]+"\n")

            print("Preparing combat...")

            for i in range (5):
                #print("TURN: "+str(i))
                attackCardHP,attackCardDMG = int(gui.cardObjects[i].get_health()), int(gui.cardObjects[i].get_damage())
                #print(str(gui.cardObjects[i].get_name())+" HP: "+str(attackCardHP)+" DMG: "+str(attackCardDMG))
                defendCardHP, defendCardDMG = int(gui.cardObjects[i+5].get_health()), int(gui.cardObjects[i+5].get_damage())
                #print(str(gui.cardObjects[i+5].get_name())+" HP: "+str(defendCardHP)+" DMG: "+str(defendCardDMG))

                #print("HOME:" +str(gui.cardObjects[i].get_name())+" lost "+str(defendCardDMG)+" HP")
                gui.cardObjects[i].losehp(defendCardDMG)
                #print("ENEMY:" +str(gui.cardObjects[i+5].get_name())+" lost "+str(attackCardDMG)+" HP")
                gui.cardObjects[i+5].losehp(attackCardDMG)
                gui.displayGUI.updateCards("")

                print(str(gui.cardObjects[5].get_health()))
