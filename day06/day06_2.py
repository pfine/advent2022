def readFine(path2file):
    inputFile = open(path2file, 'r')
    Lines = inputFile.readlines()
    return Lines

def checkIfNcharAreDiffrent(str2check,n):
    # print("   >>>-checkIfNcharAreDiffrent-> str2check = ", str2check)
    if (len(str2check) != n):
        # print("   >>>-checkIfNcharAreDiffrent-> len(str2check) = ", len(str2check))
        return False
    for ch in str2check:
        if str2check.count(ch) > 1:
            # print("   >>>-checkIfNcharAreDiffrent-> RETURN False")
            return False
    # print("   >>>-checkIfNcharAreDiffrent-> RETURN True")
    # print("   >>>-checkIfNcharAreDiffrent-> str2check = ", str2check)
    return True

def searchNDistinctCharacters(line, n):
    for i in range(n, len(line)):
        # print("  >>-searchNDistinctCharacters-> i = ", i)
        activStr2chek=line[i - n:i]
        # print("  >>-searchNDistinctCharacters-> activStr2chek = ", activStr2chek)
        if checkIfNcharAreDiffrent(activStr2chek, n):
            return i
    return len(line)

def main():
    result = 0
    path2file = './input/input_day06'
    Lines = readFine(path2file)
    Lines = [line.strip() for line in Lines]
    # print("Lines = ", Lines)

    for line in Lines:
        # print(" > line = ", line)
        startOfPacket = searchNDistinctCharacters(line, 4)
        print(" > startOfPacket = ", startOfPacket)
        # message = line[startOfPacket:]
        # print(" > message = ", message)
        startOfMessage = searchNDistinctCharacters(line, 14)
        print(" > startOfMessage = ", startOfMessage)

if __name__ == "__main__":
    main()
