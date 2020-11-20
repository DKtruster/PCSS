def sortCards(data, Log):
    dataSortHold = []
    if Log:
        print("Unsorted data: ")
        for i in range (len(data)):
            print(data[i])

    # Next 6 lines are made with help from: https://www.geeksforgeeks.org/bubble-sort/
    for lines in range(len(data)):
        for i in range(0, len(data)-lines-1):
            if int(data[i][0])>int(data[i+1][0]):
                dataSortHold = data[i].copy()
                data[i] = data[i+1]
                data[i + 1] = dataSortHold

    if Log:
        print("Sorted data: ")
        for i in range (len(data)):
            print(data[i])
        print("Sorted "+str(len(data))+" lines of data")
    return data
