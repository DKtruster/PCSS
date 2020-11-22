import random
import socket
import cards

playerCards = [[],[]]
boardArray = []
activeSockets = []

def serverSend(message):
    # Next 15 lines made with help from the lecture 7 powerpoint: "Lecture 7: Network Programming", by Jesper Rindom Jensen
    if len(activeSockets) == 0:
        s = socket.socket()
        port = 20000
        print("PORT CREATED SERVER_SENDING")
        s.bind(('', port))
        print("Socket binded to %s" % (port))
        s.listen(5)
        print("SOCKET LISTENING")
        activeSockets.append(s)

    while True:
        c, addr = activeSockets[0].accept()
        print("Got information from", addr)
        output = message
        c.sendall(output.encode("utf-8"))
        return True

def serverReceive():
    # Next 9 lines made with help from the lecture 7 powerpoint: "Lecture 7: Network Programming", by Jesper Rindom Jensen
    s = socket.socket()
    port = 20001
    print("PORT CREATED SERVER_RECEIVING")

    s.connect(('127.0.0.1', port))
    msg = s.recv(1024)
    msg = msg.decode()
    splitMsg = msg.split(' ')
    print ("[CLIENT]:",splitMsg)

    # Server loads the card numbers and sends back the name of the card numbers,
    # once the server have identifies them in the database
    nameOutputHold = []

    # Creates a new card object for each card the client sends to the server
    for i in range (5):
        strHold = cards.Cards()
        typeHold = str(splitMsg[i])
        # Initializes the card objects with new data based on the card number
        strHold.searchData(splitMsg[i])
        # Appends the card name to the array, which is later sent back
        nameOutputHold.append(str(strHold.get_name()))
        # Appends the card object to a public array, which can be accessed when running the game on the server
        playerCards[0].append(strHold)
        boardArray.append(typeHold)

    # Same content as the previous for-loop, but instead of specific card numbers, they are randomized by the computer
    # From the players perspective; this is the opponent cards being created
    for i in range (5):
        strHold = cards.Cards()
        typeHold = random.randint(0,10)
        strHold.searchData(typeHold)
        playerCards[1].append(strHold)
        boardArray.append(typeHold)

    sendEnemyBoardInfo = ("EnemyBoard "+str(boardArray[5])+" "+str(boardArray[6])+" "+str(boardArray[7])+" "+str(boardArray[8])+" "+str(boardArray[9]))
    serverSend(sendEnemyBoardInfo)

    print("PlayerObjects:",playerCards)

    outputMsg = ("Players Sent To Server:",nameOutputHold)
    return outputMsg, splitMsg, playerCards

def updatePlayersHP(board):
    # Functions updates which card objects are alive (more than 0 HP)
    playerOneCount = 0
    playerTwoCount = 0
    playersAlive = [[],[]]

    try:
        for i in range(5):
            if int(board[0][i].get_health()) > 0:
                playerOneCount += 1
                playersAlive[0].append(i)
        for i in range(5):
            if int(board[1][i].get_health()) > 0:
                playerTwoCount += 1
                playersAlive[1].append(i)
    except AttributeError: print(AttributeError)

    return playersAlive, playerOneCount-1, playerTwoCount-1


class gameRun:
    def loadCombat(self, boardArrayInput):
        roundCount = 0

        playersAlive, playerOneCount, playerTwoCount = updatePlayersHP(boardArrayInput)
        while len(playersAlive[0]) > 0 and len(playersAlive[1]) > 0:
            roundCount += 1

            # Only starts the combat if one of the two players have a card on the deck
            if playerOneCount > 0 and playerTwoCount>0:
                print("Loading board...")
                print("PlayerOne has: "+str(playerOneCount)+ " cards \n PlayerTwo has: "+str(playerTwoCount)+" cards")
                print("PlayerOne:",boardArray[0], boardArray[1], boardArray[2], boardArray[3], boardArray[4])
                print("PlayerTwo:",boardArray[5], boardArray[6], boardArray[7], boardArray[8], boardArray[9],"\n")
                print("Preparing combat...")

                for x in range(2):
                    playersAlive, playerOneCount, playerTwoCount = updatePlayersHP(boardArrayInput)
                    if x == 0 and playerOneCount > 0 and playerTwoCount > 0:
                        for i in range(playerOneCount):
                            msgSend = ""
                            if len(playersAlive[1])>0:
                                rand = int(random.randint(0, playerTwoCount-1))
                                if i == 0:
                                    print("\nYOUR TURN")

                                # Gets the attacker's and defender's card information HP and DMG
                                try: attackCardHP, attackCardDMG = int(playerCards[0][playersAlive[0][i-1]].get_health()), int(playerCards[0][playersAlive[0][i-1]].get_damage())
                                except IndexError: print("Out of bounds")
                                try: defendCardHP, defendCardDMG = int(playerCards[1][playersAlive[1][rand]].get_health()), int(playerCards[1][playersAlive[1][rand]].get_damage())
                                except IndexError: print("Out of bounds")
                                combatInfo = ("combat "+"Player0 card: "+str(i)+" attacks "+str(rand))
                                print(combatInfo)
                                serverSend(combatInfo)

                                if int(attackCardDMG) > int(defendCardHP):
                                    serverSend("[YOU] "+str(playerCards[0][playersAlive[x][i-1]].get_name()) + " kills " + str(playerCards[1][rand].get_name()))
                                    print(msgSend)

                                if int(attackCardHP) < int(defendCardDMG):
                                    serverSend("[YOU] "+str(playerCards[0][playersAlive[x][i-1]].get_name()) + " dies in an attempt to kill " + playerCards[1][rand].get_name())
                                    print(msgSend)

                                # Update the card objects with new HP based on the opponents damage
                                try: playerCards[0][playersAlive[0][i-1]].losehp(defendCardDMG)
                                except IndexError: print("Out of bounds")
                                try: playerCards[1][playersAlive[1][rand]].losehp(attackCardDMG)
                                except IndexError: print("Out of bounds")

                    playersAlive, playerOneCount, playerTwoCount = updatePlayersHP(boardArrayInput)
                    if x == 1 and playerOneCount > 0 and playerTwoCount > 0:
                        for i in range(playerTwoCount):
                            if len(playersAlive[0])>0:
                                rand = int(random.randint(0, playerOneCount-1))
                                if i == 0:
                                    print("\nENEMY TURN")
                                playersAlive, _, _ = updatePlayersHP(boardArrayInput)

                                try:attackCardHP, attackCardDMG = int(playerCards[1][playersAlive[1][i-1]].get_health()), int(playerCards[1][playersAlive[1][i-1]].get_damage())
                                except IndexError: print("Out of bounds")
                                try: defendCardHP, defendCardDMG = int(playerCards[0][playersAlive[0][rand]].get_health()), int(playerCards[0][playersAlive[0][rand]].get_damage())
                                except IndexError: print("Out of bounds")

                                combatInfo = ("combat "+"Player1 card: "+str(i)+" attacks "+str(rand))
                                print(combatInfo)
                                serverSend(combatInfo)

                                if attackCardDMG > defendCardHP:
                                    serverSend("[Enemy] " +str(playerCards[1][playersAlive[x][i-1]].get_name()) + " kills " + playerCards[0][rand].get_name())
                                if attackCardHP < defendCardDMG:
                                    serverSend("[Enemy] " +str(playerCards[1][playersAlive[x][i-1]].get_name()) + " dies in an attempt to kill " + playerCards[0][rand].get_name())

                                try: playerCards[1][playersAlive[1][i-1]].losehp(defendCardDMG)
                                except IndexError: print("Out of bounds")
                                try:playerCards[0][playersAlive[0][rand]].losehp(attackCardDMG)
                                except IndexError: print("Out of bounds")

            playersAlive, playerOneCount, playerTwoCount = updatePlayersHP(playerCards)
            if playerOneCount > 0 and playerTwoCount == 0:
                serverSend("You won!")
                serverSend("Close")
                print("Game ended")

            if playerOneCount == 0 and playerTwoCount > 0:
                serverSend("You lost")
                serverSend("Close")
                print("Game ended")

            if playerOneCount == 0 and playerTwoCount == 0:
                serverSend("It's a tie!")
                serverSend("Close")
                print("Game ended")

            msgTest = "round count:"+str(roundCount)
            serverSend(msgTest)

    get = False
    msgSend = "Connected to server"
    msgRecv = ""

    counter = 0

    while True & counter < 1:
        get = serverSend(msgSend)
        # If the server establishes connection to the client the following code block runs once
        if get & counter < 1:
            # The array of card objects is being received, which starts the combat
            msgToSend, msgRecv, playerCards = serverReceive()
            print(msgRecv)
            loadCombat("", (playerCards))
            get = True
            counter+= 1
