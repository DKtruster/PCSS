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
        # c.close()
        return True

def serverReceive():
    s = socket.socket()
    port = 20001
    print("PORT CREATED SERVER_RECEIVING")

    s.connect(('127.0.0.1', port))
    msg = s.recv(1024)
    msg = msg.decode()
    splitMsg = msg.split(' ')
    print (splitMsg)
    # s.close()

    nameOutputHold = []

    for i in range (5):
        strHold = cards.Cards()
        typeHold = str(splitMsg[i])
        strHold.searchData(splitMsg[i])
        nameOutputHold.append(str(strHold.get_name()))
        playerCards[0].append(strHold)
        boardArray.append(typeHold)

    for i in range (5):
        strHold = cards.Cards()
        typeHold = random.randint(0,10)
        strHold.searchData(int(2))
        # nameOutputHold.append(str(strHold.get_name()))
        playerCards[1].append(strHold)
        boardArray.append(typeHold)

    print("PlayerObjects:",playerCards)

    outputMsg = ("Players Sent To Server:",nameOutputHold)
    return outputMsg, splitMsg

def updatePlayersHP(board):
    playerOneCountTT = 0
    playerTwoCount = 0
    playersAlive = [[],[]]

    # print("Player HP List:",playerCards.get_health())
    print("BoardUpdateHP",board)

    try:
        for i in range(5):
            if board[i] != "":
                print("Try:AddingOne to",playerOneCountTT)
                playerOneCountTT += 1
                playersAlive.append(i)
                print("health:",board[i])
                print(i,playerCards[0][i].get_health(),playerCards[0][i].get_name())
    except IndexError:
        for i in range(5):
            print("HPTEST",board[0][i].get_health())
            if board[0][i] != "":
                print("Except:AddingOne to",playerOneCountTT)
                playerOneCountTT += 1
                playersAlive.append(i)
                print("health:",board[0][i])
                print(i,playerCards[0][i].get_health(),playerCards[0][i].get_name())

    print("FinalPlayerCount:",playerOneCountTT)
    # for i in range(5):
    #     if board[i + 5] != "":
    #         playerTwoCount = playerTwoCount + 1
    #         playersAlive[1].append(i+5)
    #         print("health:",board[i+5])
    #         print(i,playerCards[1][i].get_health(),playerCards[1][i].get_name())


    return playersAlive, playerOneCountTT, playerTwoCount


class gameRun:
    def loadCombat(self, boardArrayInput):
        playersAlive, playerOneCount, playerTwoCount = updatePlayersHP(boardArrayInput)
        print("PlayeOneCount: "+str(playerOneCount), " PlayerTwoCount: "+str(playerTwoCount))

        # Only starts the combat if one of the two players have a card on the deck
        if playerOneCount > 0 and playerTwoCount>0:
            print("Loading board...")
            print("PlayerOne has: "+str(playerOneCount)+ " cards \n PlayerTwo has: "+str(playerTwoCount)+" cards")
            print("PlayerOne:",boardArray[0], boardArray[1], boardArray[2], boardArray[3], boardArray[4])
            print("PlayerTwo:",boardArray[5], boardArray[6], boardArray[7], boardArray[8], boardArray[9],"\n")

            print("Preparing combat...")

            for x in range(2):
                playersAlive, playerOneCount, playerTwoCount = updatePlayersHP(boardArrayInput)
                for i in range (len(playersAlive[x])):
                    playersAlive, playerOneCount, playerTwoCount = updatePlayersHP(boardArrayInput)
                    print("PlayersAlive:",playersAlive)
                    if x == 0:
                        msgSend = "test"
                        if len(playersAlive[1])>0:
                            rand = int(random.randint(0, (len(playersAlive[1]))-1))
                            if i == 0:
                                print("\nYOUR TURN")

                            attackCardHP, attackCardDMG = int(playerCards[0][playersAlive[0][i]].get_health()), int(playerCards[0][playersAlive[0][i]].get_damage())
                            defendCardHP, defendCardDMG = int(playerCards[1][playersAlive[1][rand]-5].get_health()), int(playerCards[1][playersAlive[1][rand]-5].get_damage())

                            print("AttackcardDMG",attackCardHP,"DefendcardHP",defendCardHP)
                            if int(attackCardDMG) > int(defendCardHP):
                                print("Yup")
                                print(str(playerCards[playersAlive[x][i]].get_name()) + " kills " + playerCards[rand+5].get_name())
                                msgSend=(str(playerCards[playersAlive[x][i]].get_name()) + " kills " + playerCards[rand+5].get_name())
                                print(msgSend)

                            if int(attackCardHP) < int(defendCardDMG):
                                print("Yup")
                                print(str(playerCards[playersAlive[x][i]].get_name()) + " dies in an attempt to kill " + playerCards[rand+5].get_name())
                                msgSend=(str(playerCards[playersAlive[x][i]].get_name()) + " dies in an attempt to kill " + playerCards[rand+5].get_name())
                                print(msgSend)

                            playerCards[0][playersAlive[x][i]].losehp(defendCardDMG)
                            playerCards[1][playersAlive[1][rand]-5].losehp(attackCardDMG)

                    if x == 1:
                        if len(playersAlive[0])>0:
                            rand = int(random.randint(0, (len(playersAlive[0]))-1))
                            if i == 0:
                                print("\nENEMY TURN")
                            attackCardHP, attackCardDMG = int(playerCards[1][playersAlive[1][i]-5].get_health()), int(playerCards[1][playersAlive[1][i]-5].get_damage())
                            defendCardHP, defendCardDMG = int(playerCards[0][playersAlive[0][rand]].get_health()), int(playerCards[0][playersAlive[0][rand]].get_damage())

                            if attackCardDMG > defendCardHP:
                                msgSend=(str(playerCards[playersAlive[x][i]].get_name()) + " kills " + playerCards[rand].get_name())
                            if attackCardHP < defendCardDMG:
                                msgSend=(str(playerCards[playersAlive[x][i]].get_name()) + " dies in an attempt to kill " + playerCards[rand].get_name())

                            playerCards[1][playersAlive[1][i]-5].losehp(defendCardDMG)
                            playerCards[0][playersAlive[0][rand]].losehp(attackCardDMG)
                    serverSend(msgSend)

        playersAlive, playerOneCount, playerTwoCount = updatePlayersHP(playerCards)
        print("PlayerOneCount",playerOneCount,"PlayerTwoCount",playerTwoCount)
        if playerOneCount > 0 and playerTwoCount == 0:
            serverSend("Server: You won!")

        if playerOneCount == 0 and playerTwoCount > 0:
            serverSend("Server: You lost")

        if playerOneCount == 0 and playerTwoCount == 0:
            serverSend("Server: It's a tie!")

    get = False
    ifConnected = False
    msgSend = "Connected to server"
    msgRecv = ""

    counter = 0

    while True & counter < 1:
        # print("Sending new...")
        get = serverSend(msgSend)

        if get & counter < 1:
            print("Receiving new...")
            msgToSend, msgRecv = serverReceive()
            print(msgRecv)
            loadCombat("", (msgRecv))
            get = True
            counter+= 1
