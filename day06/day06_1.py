def readFine(path2file):
    inputFile = open(path2file, 'r')
    Lines = inputFile.readlines()
    return Lines

def checkIf4charAreDiffrent(str2check):
    # print("   >>>-checkIf4charAreDiffrent-> str2check = ", str2check)
    if (len(str2check) != 4):
        # print("   >>>-checkIf4charAreDiffrent-> len(str2check) = ", len(str2check))
        return False
    for ch in str2check:
        if str2check.count(ch) > 1:
            # print("   >>>-checkIf4charAreDiffrent-> RETURN False")
            return False
    # print("   >>>-checkIf4charAreDiffrent-> RETURN True")
    # print("   >>>-checkIf4charAreDiffrent-> str2check = ", str2check)
    return True

def search4initSequence(line):
    for i in range(4, len(line)):
        # print("  >>-search4initSequence-> i = ", i)
        activStr2chek=line[i - 4:i]
        # print("  >>-search4initSequence-> activStr2chek = ", activStr2chek)
        if checkIf4charAreDiffrent(activStr2chek):
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
        result = search4initSequence(line)


    print("result = ", result)

if __name__ == "__main__":
    main()
