import numpy as np
import bubblesort
import binarysearch

dataLoader = np.genfromtxt('origins.txt', dtype='str')


class Cards:
    __cardnumber = "0"
    __price = "0"
    __name = "NameHold"
    __origin = "OriginHold"
    __health = 0
    __damage = 0


    # TO-DO: Add binary search
    def searchData(self, cardNumber):
        sortedCards = bubblesort.sortCards(dataLoader, False)
        arrayPosCard = binarysearch.binarysearch(sortedCards, cardNumber)

        # 404 is a default value, if it returns this number it means it haven't found anything
        if arrayPosCard != 404:
            print("Defining cardNumber:",cardNumber)
            self.__cardnumber = sortedCards[arrayPosCard][0]
            self.__price = sortedCards[arrayPosCard][1]
            self.__name = sortedCards[arrayPosCard][2]
            self.__origin = sortedCards[arrayPosCard][3]
            self.__health = sortedCards[arrayPosCard][5]
            self.__damage = sortedCards[arrayPosCard][4]


    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_damage(self):
        return self.__damage

    def get_origin(self):
        return self.__origin

    def losehp(self, losthp):
        self.__health = int(self.__health)-int(losthp)
