class Cards:
    __cardnumber = "0"
    __name = "NameHold"
    __origin = "OriginHold"
    __health = "10"
    __damage = "5"

    def __init__(self, cardnumber: int , name: str, origin: str, health: int, damage: int):
        self.__cardnumber = cardnumber
        self.__name = name
        self.__origin = origin
        self.__health = health
        self.__damage = damage

    def get_name(self):
        return self.__name


