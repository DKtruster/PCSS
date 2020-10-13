import gui
import random

def updatePlayersHP(board):
    playerOneCount = 0
    playerTwoCount = 0
    playersAlive = [[],[]]

    for i in range(5):
        if board[i] != "":
            playerOneCount = playerOneCount + 1
            playersAlive[0].append(i)

    for i in range(5):
        if board[i + 5] != "":
            playerTwoCount = playerTwoCount + 1
            playersAlive[1].append(i+5)

    return playersAlive, playerOneCount, playerTwoCount


class gameRun:
    def loadCombat(self, boardArray):
        playersAlive, playerOneCount, playerTwoCount = updatePlayersHP(boardArray)
        print("PlayeOneCount: "+str(playerOneCount), " PlayerTwoCount: "+str(playerTwoCount))

        # Only starts the combat if one of the two players have a card on the deck
        if playerOneCount > 0 or playerTwoCount>0:
            print("Loading board...")
            print("PlayerOne has: "+str(playerOneCount)+ " cards \n PlayerTwo has: "+str(playerTwoCount)+" cards")
            print("PlayerOne: "+boardArray[0], boardArray[1], boardArray[2], boardArray[3], boardArray[4])
            print("PlayerTwo: "+boardArray[5], boardArray[6], boardArray[7], boardArray[8], boardArray[9]+"\n")

            print("Preparing combat...")

            for x in range(2):
                playersAlive, playerOneCount, playerTwoCount = updatePlayersHP(gui.boardArray)
                for i in range (len(playersAlive[x])):
                    if x == 0:
                        if len(playersAlive[1])>0:
                            rand = random.randint(0, (len(playersAlive[1])+4))
                        if i == 0:
                            print("YOUR TURN")
                    if x == 1:
                        if len(playersAlive[0])>0:
                            rand = random.randint(0, (len(playersAlive[0]) - 1))
                        if i == 0:
                            print("ENEMY TURN")

                    #print(str(gui.cardObjects[playersAlive[x][i]].get_name()) + " attacks "+ gui.cardObjects[rand].get_name())

                    attackCardHP, attackCardDMG = int(gui.cardObjects[playersAlive[x][i]].get_health()), int(gui.cardObjects[playersAlive[x][i]].get_damage())
                    defendCardHP, defendCardDMG = int(gui.cardObjects[rand].get_health()), int(gui.cardObjects[rand].get_damage())

                    if attackCardDMG > defendCardHP:
                        print(str(gui.cardObjects[playersAlive[x][i]].get_name()) + " kills " + gui.cardObjects[rand].get_name())
                    if attackCardHP < defendCardDMG:
                        print(str(gui.cardObjects[playersAlive[x][i]].get_name()) + " dies to " + gui.cardObjects[rand].get_name()+ " in an attempt to kill")

                    gui.cardObjects[playersAlive[x][i]].losehp(defendCardDMG)
                    gui.cardObjects[rand].losehp(attackCardDMG)
                gui.displayGUI.updateCards("")
