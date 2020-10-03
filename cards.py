import numpy as np

cardNames = []
dataLoader = np.genfromtxt('origins.txt', dtype='str')

def loadCards():
    # Data loader from .txt files made with help from:
    # https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/numpy-arrays/import-txt-csv-files-numpy-arrays/
    for lines in range(len(dataLoader)):
        cardNames.append(dataLoader[lines][1])
        cardNames[lines] = dataLoader[lines][0], dataLoader[lines][1], dataLoader[lines][2],dataLoader[lines][3], dataLoader[lines][4], dataLoader[lines][5], dataLoader[lines][6], dataLoader[lines][7]
    #print(dataLoader[lines])

def returnCard(cardNumber):
    return dataLoader[cardNumber]

class Cards:
    __cardnumber = "0"
    __price = "0"
    __name = "NameHold"
    __origin = "OriginHold"
    __health = "0"
    __damage = "0"
    __cardImg = "CDviking1"
    __shopImg = "CDviking1"


    def searchData(self, cardName):
        loadCards()
        for i in range (len(cardNames)-1):
            if cardNames[i][0]==cardName:
                self.__cardnumber = cardNames[i][0]
                self.__price = cardNames[i][1]
                self.__name = cardNames[i][2]
                self.__origin = cardNames[i][3]
                self.__health = cardNames[i][4]
                self.__damage = cardNames[i][5]
                self.__cardImg = cardNames[i][6]
                self.__shopImg = cardNames[i][7]
                print("Data successfully loaded for: "+cardName)
                return



    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_damage(self):
        return self.__damage

    def get_origin(self):
        return self.__origin

    def get_cardImg(self):
        return self.__cardImg

    def get_shopImg(self):
        return self.__shopImg
