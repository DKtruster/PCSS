def sortCards(data, Log):
    # If this method is called requiring a log of the data being sorted, the content of the if-statement will run
    if Log:
        print("Unsorted data: ")
        for i in range (len(data)):
            print(data[i])

    # Next 6 lines of code are made with help from: https://www.geeksforgeeks.org/bubble-sort/
    for lines in range(len(data)):
        # For each data position that has already been sorted will be skipped in the upcoming
        # iterations of the for-loop with the (-lines-1) statement.
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
