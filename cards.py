import numpy as np

dataLoader = np.genfromtxt('origins.txt', dtype='str')

# TO-DO: Implement graphics for more cards


def sortCards(Log):
    dataSortHold = []
    if Log:
        print("Unsorted data: ")
        for i in range (len(dataLoader)):
            print(dataLoader[i])

    # Next 6 lines are made with help from: https://www.geeksforgeeks.org/bubble-sort/
    for lines in range(len(dataLoader)):
        for i in range(0, len(dataLoader)-lines-1):
            if int(dataLoader[i][0])>int(dataLoader[i+1][0]):
                dataSortHold = dataLoader[i].copy()
                dataLoader[i] = dataLoader[i+1]
                dataLoader[i + 1] = dataSortHold

    if Log:
        print("Sorted data: ")
        for i in range (len(dataLoader)):
            print(dataLoader[i])
        print("Sorted "+str(len(dataLoader))+" lines of data")
    return True


class Cards:
    __cardnumber = "0"
    __price = "0"
    __name = "NameHold"
    __origin = "OriginHold"
    __health = 0
    __damage = 0


    # TO-DO: Add binary search
    def searchData(self, cardNumber):
        sortCards(False)
        middleLen = round(len(dataLoader) / 2)-1
        middleNum = dataLoader[middleLen][0]
        if cardNumber < middleNum:
            for i in range (0,middleLen):
                if dataLoader[i][0]==cardNumber:
                    self.__cardnumber = dataLoader[i][0]
                    self.__price = dataLoader[i][1]
                    self.__name = dataLoader[i][2]
                    self.__origin = dataLoader[i][3]
                    self.__health = dataLoader[i][5]
                    self.__damage = dataLoader[i][4]
                    # print("Found: "+cardNumber+" in lower array stack")
                    return
        if int(cardNumber) >= int(middleNum):
            for i in range (int(middleNum),len(dataLoader)):
                if dataLoader[i][0]==cardNumber:
                    self.__cardnumber = dataLoader[i][0]
                    self.__price = dataLoader[i][1]
                    self.__name = dataLoader[i][2]
                    self.__origin = dataLoader[i][3]
                    self.__health = dataLoader[i][5]
                    self.__damage = dataLoader[i][4]
                    # print("Found: "+cardNumber + " in upper array stack")
                    return

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_damage(self):
        return self.__damage

    def get_origin(self):
        return self.__origin

    def losehp(self, losthp):
        self.__health = int(self.__health)-losthp

    def test(self):
        return self.__damage
