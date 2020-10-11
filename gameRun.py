import gui

runcheck = False
player1Count = 0
player2Count = 0


class gameRun:
    def loadCombat(self, boardArray, runCheck):
        runcheck = runCheck
        print(runcheck)
        if (runcheck):
            print("Loading combat...")
            print(boardArray[0][0],boardArray[0][1],boardArray[0][2],boardArray[0][3],boardArray[0][4])
            print(boardArray[1][5],boardArray[1][6],boardArray[1][7],boardArray[1][8],boardArray[1][9])

        for x in range (2):
            for i in range (5):
                if boardArray[x][i] != "":
                    strHold = "player"+x+"Count"
                    strHold = strHold+1

        if boardArray[1][6] != "":
            print(boardArray[1][6])
            print(str(gui.cardObjects[0].get_health()))