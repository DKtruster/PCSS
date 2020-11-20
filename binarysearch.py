def binarysearch(sortedCards, cardNumber):
    middleLen = round(len(sortedCards) / 2)-1
    middleNum = sortedCards[middleLen][0]

    arrayPos = 404

    if int(cardNumber) < int(middleNum):
        for i in range (0,middleLen):
            if int(sortedCards[i][0]) == int(cardNumber):
                arrayPos = i

    elif int(cardNumber) >= int(middleNum):
        for i in range(int(middleNum), len(sortedCards)):
            if int(sortedCards[i][0]) == int(cardNumber):
                arrayPos = i

    return arrayPos
