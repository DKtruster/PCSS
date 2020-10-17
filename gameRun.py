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
        # print("PlayeOneCount: "+str(playerOneCount), " PlayerTwoCount: "+str(playerTwoCount))

        # Only starts the combat if one of the two players have a card on the deck
        if playerOneCount > 0 and playerTwoCount>0:
            print("Loading board...")
            # print("PlayerOne has: "+str(playerOneCount)+ " cards \n PlayerTwo has: "+str(playerTwoCount)+" cards")
            # print("PlayerOne: "+boardArray[0], boardArray[1], boardArray[2], boardArray[3], boardArray[4])
            # print("PlayerTwo: "+boardArray[5], boardArray[6], boardArray[7], boardArray[8], boardArray[9]+"\n")

            print("Preparing combat...")

            for x in range(2):
                playersAlive, playerOneCount, playerTwoCount = updatePlayersHP(gui.boardArray)
                for i in range (len(playersAlive[x])):
                    playersAlive, playerOneCount, playerTwoCount = updatePlayersHP(gui.boardArray)
                    if x == 0:
                        if len(playersAlive[1])>0:
                            rand = int(random.randint(0, (len(playersAlive[1]))-1))
                            if i == 0:
                                print("\nYOUR TURN")
                            attackCardHP, attackCardDMG = int(gui.cardObjects[playersAlive[0][i]].get_health()), int(gui.cardObjects[playersAlive[0][i]].get_damage())
                            defendCardHP, defendCardDMG = int(gui.cardObjects[playersAlive[1][rand]].get_health()), int(gui.cardObjects[playersAlive[1][rand]].get_damage())

                            if attackCardDMG > defendCardHP:
                                print(str(gui.cardObjects[playersAlive[x][i]].get_name()) + " kills " + gui.cardObjects[rand+5].get_name())
                            if attackCardHP < defendCardDMG:
                                print(str(gui.cardObjects[playersAlive[x][i]].get_name()) + " dies in an attempt to kill " + gui.cardObjects[rand+5].get_name())

                            gui.cardObjects[playersAlive[x][i]].losehp(defendCardDMG)
                            gui.cardObjects[playersAlive[1][rand]].losehp(attackCardDMG)

                    if x == 1:
                        if len(playersAlive[0])>0:
                            rand = int(random.randint(0, (len(playersAlive[0]))-1))
                            #rand = 4
                            if i == 0:
                                print("\nENEMY TURN")
                            attackCardHP, attackCardDMG = int(gui.cardObjects[playersAlive[1][i]].get_health()), int(gui.cardObjects[playersAlive[1][i]].get_damage())
                            defendCardHP, defendCardDMG = int(gui.cardObjects[playersAlive[0][rand]].get_health()), int(gui.cardObjects[playersAlive[0][rand]].get_damage())

                            if attackCardDMG > defendCardHP:
                                print(str(gui.cardObjects[playersAlive[x][i]].get_name()) + " kills " + gui.cardObjects[rand].get_name())
                            if attackCardHP < defendCardDMG:
                                print(str(gui.cardObjects[playersAlive[x][i]].get_name()) + " dies in an attempt to kill " + gui.cardObjects[rand].get_name())

                            gui.cardObjects[playersAlive[x][i]].losehp(defendCardDMG)
                            gui.cardObjects[playersAlive[0][rand]].losehp(attackCardDMG)

                gui.displayGUI.updateCards("")

        playersAlive, playerOneCount, playerTwoCount = updatePlayersHP(gui.boardArray)
        if playerOneCount > 0 and playerTwoCount == 0:
            print("You won!")

        if playerOneCount == 0 and playerTwoCount > 0:
            print("You lost")

        if playerOneCount == 0 and playerTwoCount == 0:
            print("It's a tie!")
