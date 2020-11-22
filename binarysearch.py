def binarysearch(sortedCards, cardNumber):
    # Finds the middle number of the length of the dataset
    middleLen = round(len(sortedCards) / 2)-1
    middleNum = sortedCards[middleLen][0]

    # 404 is a default placeholder number, which is updated if the function finds the correct position in the dataset
    # if the function passes "404" it means it have not found the number in the dataset, since it is not updated
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
