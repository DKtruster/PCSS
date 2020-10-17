import numpy as np

dataLoader = np.genfromtxt('origins.txt', dtype='str')

# TO-DO: Implement a sorting algorithm for an unorganised .txt file
# TO-DO: Make 17 more cards

def sortCards():
    dataSortHold = []
    print("Unsorted data: ")
    for i in range (len(dataLoader)):
        print(dataLoader[i])

    # Next 6 lines are made with help from: https://www.geeksforgeeks.org/bubble-sort/
    for lines in range(len(dataLoader)):
        for i in range(0, len(dataLoader)-lines-1):
            if dataLoader[i][0]>dataLoader[i+1][0]:
                dataSortHold = dataLoader[i].copy()
                dataLoader[i] = dataLoader[i+1]
                dataLoader[i + 1] = dataSortHold

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
        for i in range (len(dataLoader)):
            if dataLoader[i][0]==cardNumber:
                self.__cardnumber = dataLoader[i][0]
                self.__price = dataLoader[i][1]
                self.__name = dataLoader[i][2]
                self.__origin = dataLoader[i][3]
                self.__health = dataLoader[i][5]
                self.__damage = dataLoader[i][4]
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
