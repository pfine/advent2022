def readFine(path2file):
    inputFile = open(path2file, 'r')
    Lines = inputFile.readlines()
    return Lines

def inCommandBlockExec(currentPath, currentCommandBlock):
    # print("   >>>-inCommandBlockExec-> currentPath:", currentPath)
    # print("   >>>-inCommandBlockExec-> currentCommandBlock:", currentCommandBlock)
    size = 0
    isDirHere = False
    dirPath2Add = ""
    for line in currentCommandBlock:
        if line.startswith("dir "):
            isDirHere = True
            if currentPath == "/":
                dirPath2Add = dirPath2Add + "+" + currentPath + line.split()[-1]
            else: 
                dirPath2Add = dirPath2Add + "+" + currentPath + "/" + line.split()[-1]
            continue
        size = size + int(line.split()[0])

    # print("   >>>-inCommandBlockExec-> END isDirHere =", isDirHere)
    # print("   >>>-inCommandBlockExec-> END size =", size)
    # print("   >>>-inCommandBlockExec-> END dirPath2Add =", dirPath2Add)
    if isDirHere:
        return str(size) + dirPath2Add
    return size


def pathBuilder(currentPath, modyfyWith):
    # print("   >>>-pathBuilder-> currentPath =", currentPath)
    # print("   >>>-pathBuilder-> modyfyWith =", modyfyWith)
    if modyfyWith == "..": # go back with path
        currentPathArray = currentPath.split("/")
        # print("   >>>-pathBuilder-> currentPathArray =", currentPathArray)
        currentPath = "/".join(currentPathArray[:-1])
        # print("   >>>-pathBuilder-> RETURN .. currentPath =", currentPath)
        return currentPath
    elif modyfyWith == "/":
        currentPath = modyfyWith
        # print("   >>>-pathBuilder-> RETURN MOVE to: / currentPath =", currentPath)
        return currentPath
    # prepare result
    if currentPath == "/":
        currentPath = currentPath + modyfyWith
    else:
        currentPath = currentPath + "/" + modyfyWith
    # print("   >>>-pathBuilder-> RETURN Add / currentPath =", currentPath)
    return currentPath

def isStillSumUpInResult(result):
    for dirPath in result:
        # print("   >>>-isStillSumUpInResult-> dirPath =", dirPath)
        # print("   >>>-isStillSumUpInResult-> size =", result[dirPath])
        if str(result[dirPath]).count("+") != 0:
            return True
    return False


def main():
    path2file = './input/input_day07'
    Lines = readFine(path2file)
    Lines = [line.strip() for line in Lines]
    print("Lines =", Lines)

    allFoldersDirectory = {} # dict
    inCommandBlock = False
    currentPath = "" # string
    currentCommandBlock = [] # array

    for line in Lines:
        print(" > currentPath =", currentPath)
        print(" > line =", line)
        if line.startswith("$ "): # new command
            # count existing path size
            if inCommandBlock:
                size = inCommandBlockExec(currentPath, currentCommandBlock)
                # print("  >> size:", size)
                allFoldersDirectory[currentPath] = size
                # print("  >> allFoldersDirectory[", currentPath,"]:", size)
                # print("  >> currentPath[", currentPath)
                inCommandBlock = False
                currentCommandBlock = []

            # execute the command part
            if line.startswith("$ cd"):
                # print("  >> Change Directory:", line)
                # print("  >> currentPath[", currentPath)
                currentPath = pathBuilder(currentPath, line.split()[-1])
                inCommandBlock = False
            elif line.startswith("$ ls"):
                inCommandBlock = True
                # print("  >> currentCommandBlock:", currentCommandBlock)
                currentCommandBlock = []
                # print("  >> List Directory:", line)
            else:
                print(" Sth worng !!!")
                return 1
        else: # in command block
            currentCommandBlock.append(line)
            # print("  >> currentPath:", currentPath)
            # print("  >> currentCommandBlock:", currentCommandBlock)
            continue
    # post processing if sth left in currentCommandBlock
    if inCommandBlock:
        # print(" > POST: currentPath =", currentPath)
        # print(" > POST: inCommandBlock =", inCommandBlock)
        # print(" > POST: currentCommandBlock =", currentCommandBlock)
        size = inCommandBlockExec(currentPath, currentCommandBlock)
        # print(" > POST: size:", size)
        allFoldersDirectory[currentPath] = size
        # print(" > POST: allFoldersDirectory[", currentPath,"]:", size)
        # print(" > POST: currentPath[", currentPath)
        inCommandBlock = False
        currentCommandBlock = []

    print(" > POST: allFoldersDirectory[", allFoldersDirectory)

    # final sum-up needed - replace folder with summend size
    needToCleanSumFromResultDirectory = True
    while needToCleanSumFromResultDirectory:
        for dirPath in allFoldersDirectory:
            # print(" > SUM-UP: dirPath =", dirPath)
            # print(" > SUM-UP: size =", allFoldersDirectory[dirPath])
            if str(allFoldersDirectory[dirPath]).count("+") != 0:
                splitAgain = allFoldersDirectory[dirPath].split("+")
                # print(" > SUM-UP: splitAgain =", splitAgain)
                for i, partDir in enumerate(splitAgain):
                    # print(" > SUM-UP: i =", i)
                    # print(" > SUM-UP: partDir =", partDir)
                    if (partDir.count("/") != 0) and (partDir in allFoldersDirectory.keys()) and (str(allFoldersDirectory[partDir]).count("+") == 0):
                        # print("   > SUM-UP: allFoldersDirectory[partDir] =", allFoldersDirectory[partDir])
                        # print("   > SUM-UP: BEFORE splitAgain[i] =", splitAgain[i])
                        splitAgain[i] = str(allFoldersDirectory[partDir])
                        # print("   > SUM-UP: AFTER splitAgain[i] =", splitAgain[i])
                joinAgain = "+".join(splitAgain)
                # print(" > SUM-UP: joinAgain =", joinAgain)
                if str(joinAgain).count("/") == 0:
                    allFoldersDirectory[dirPath] = eval(joinAgain)
                else:
                    allFoldersDirectory[dirPath] = joinAgain
                # print(" > SUM-UP: allFoldersDirectory =", allFoldersDirectory)
        needToCleanSumFromResultDirectory = isStillSumUpInResult(allFoldersDirectory)

    print("allFoldersDirectory =", allFoldersDirectory)

    # Find sime of firs with size lower then 100 000 
    rsult = 0
    for dirPath in allFoldersDirectory:
        print(" > POST-PROCESSING: dirPath =", dirPath)
        print(" > POST-PROCESSING: size =", allFoldersDirectory[dirPath])
        if allFoldersDirectory[dirPath] < 100000:
            rsult = rsult + allFoldersDirectory[dirPath]

    print("rsult =", rsult)

if __name__ == "__main__":
    main()
