def readFine(path2file):
    inputFile = open(path2file, 'r')
    Lines = inputFile.readlines()
    return Lines

def printStacksState(stackState):
    i = 1
    for line in stackState:
        print(i, ":", line)
        i += 1

# [N]     [C]                 [Q]    
# [W]     [J] [L]             [J] [V]
# [F]     [N] [D]     [L]     [S] [W]
# [R] [S] [F] [G]     [R]     [V] [Z]
# [Z] [G] [Q] [C]     [W] [C] [F] [G]
# [S] [Q] [V] [P] [S] [F] [D] [R] [S]
# [M] [P] [R] [Z] [P] [D] [N] [N] [M]
# [D] [W] [W] [F] [T] [H] [Z] [W] [R]
#  1   2   3   4   5   6   7   8   9 
def initStackState(initStateRead):
    workArray = initStateRead[::-1]
    indexReadPattern = []
    print(" initStateRead =")
    for i in initStateRead:
        print(i.rstrip())
    # read indexes that contais crate letter
    for index, char in enumerate(workArray[0]):
        if not char.isspace():
            # print("   >>> index = ", index)
            # print("   >>> char = ", char)
            indexReadPattern.append(index)
    # print("  >> indexReadPattern = ", indexReadPattern)
    curretCratesPileState = [""] * len(indexReadPattern)
    # print("   >>> curretCratesPileState = ", curretCratesPileState)
    for i in range(1,len(workArray)):
        currentProcessLine = workArray[i]
        # print("   >>> currentProcessLine = ", currentProcessLine)
        for index, value in enumerate(indexReadPattern):
            # print("   >>> index = ", index)
            # print("   >>> value = ", value)
            # print("   >>> currentProcessLine[", value,"] = ", currentProcessLine[value])
            # print("   >>> curretCratesPileState[", index,"] = ", curretCratesPileState[index])
            currentCrate = currentProcessLine[value]
            # print("   >>> currentCrate = ", currentCrate)
            if currentCrate != ' ':
                # print("   >>>--> IN ")
                curretCratesPileState[index] = curretCratesPileState[index] + currentCrate
            # print("   >>> curretCratesPileState = ", curretCratesPileState)
            # return []
    # print("   >>> curretCratesPileState = ", curretCratesPileState)

    return curretCratesPileState

def listLastCharOfStringArray(arrayOfStrings):
    result = ''
    for string in arrayOfStrings:
        result = result + string[-1]
    return result

def moveCrain(stackState, repeatTimes, takeFromStack, placeToStack):
    # print("  >>>-moveCrain-> stackState =", stackState)
    for repet in range (0, repeatTimes):
        # print("  >>>-moveCrain-> repet =", repet)
        # take FROM - remove last element
        # print("  >>>-moveCrain-> BEFOR stackState[", takeFromStack, "] =", stackState[takeFromStack])
        moveingElem = stackState[takeFromStack][-1]
        # print("  >>>-moveCrain-> moveingElem =", moveingElem)
        stackState[takeFromStack] = stackState[takeFromStack][:-1]
        # print("  >>>-moveCrain-> AFTER stackState[", takeFromStack, "] =", stackState[takeFromStack])
        # place TO - add as last elemrnt
        # print("  >>>-moveCrain-> BEFOR stackState[", placeToStack, "] =", stackState[placeToStack])
        stackState[placeToStack] = stackState[placeToStack] + moveingElem
        # print("  >>>-moveCrain-> AFTER stackState[", placeToStack, "] =", stackState[placeToStack])
        # printStacksState(stackState)
    return stackState

def main():
    path2file = './input/input_day05.txt'
    Lines = readFine(path2file)
    # Lines = [line.strip() for line in Lines]
    # print("Lines = ", Lines)
    initStateRead = []
    moveData = False
    for line in Lines:
        if (not moveData) and (line != '\n'):
            initStateRead.append(line)
            continue
        elif (not moveData) and (line == '\n'):
            stackState = initStackState(initStateRead)
            moveData = True
            # print(" > initStateRead = ", initStateRead)
            # print(" > stackState = ", stackState)
            continue
        line = line.strip()
        # print(" > line = ", line)
        # print(" > line.split() = ", line.split())
        # change state according to the move section
        divdeLine = line.split()
        repeatTimes = int(divdeLine[1])
        takeFromStack = int(divdeLine[3]) - 1 # index from 0
        placeToStack = int(divdeLine[5]) - 1 # index from 0
        # print(" > repeatTimes, takeFromStack, placeToStack = ", repeatTimes, takeFromStack, placeToStack)
        stackState = moveCrain(stackState, repeatTimes, takeFromStack, placeToStack)

    # print(" stackState = ", stackState)
    print("\n Final stackState:")
    printStacksState(stackState)
    result = listLastCharOfStringArray(stackState)
    print("\n result = ", result)

if __name__ == "__main__":
    main()
