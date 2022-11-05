from array import array


def printArray(Array):
    lenn = len(Array)
    for i in range(lenn):
        print(Array.index(i))

myArray = array('i')
for i in range(5):
    myArray.append(i)



printArray(myArray)



    
myArray.remove(0)

printArray(myArray)