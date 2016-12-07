def bubbleSort(myList):
    for i in range (0, len(myList) - 1):
        for j in range (0, len(myList) - 1 - i):
            if myList[j] > myList[j+1]:
                myList[j], myList[j+1] = myList[j+1], myList[j]
    return myList

theList = [89, 23, 33, 45, 10, 12, 45, 45, 45]
print(bubbleSort(theList))