import numpy as np

cardNames = []


def loadCards():
    # Data loader from .txt files made with help from:
    # https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/numpy-arrays/import-txt-csv-files-numpy-arrays/
    dataLoader = np.genfromtxt('origins.txt', dtype='str')

    for lines in range(len(dataLoader)):
        cardNames.append(dataLoader[lines][1])
        cardNames[lines] = Cards(dataLoader[lines][0], dataLoader[lines][1], dataLoader[lines][2],dataLoader[lines][3], dataLoader[lines][4], dataLoader[lines][5])

        print(dataLoader[lines])



class Cards:
    __cardnumber = "0"
    __price = "0"
    __name = "NameHold"
    __origin = "OriginHold"
    __health = "0"
    __damage = "0"

    def __init__(self, cardnumber: int, price: int, name: str, origin: str, health: int, damage: int):
        self.__cardnumber = cardnumber
        self.__price = price
        self.__name = name
        self.__origin = origin
        self.__health = health
        self.__damage = damage

    def get_name(self):
        return self.__name

    def get_origin(self):
        return self.__origin