def readFine(path2file):
    inputFile = open(path2file, 'r')
    Lines = inputFile.readlines()
    return Lines

# To help prioritize item rearrangement, every item type can be converted to a priority:
    # - Lowercase item types a through z have priorities 1 through 26.
    # - Uppercase item types A through Z have priorities 27 through 52.
def encodeLetter2Priority(letter):
    # print("   >>> letter = ", letter)
    encode2Ascii = ord(letter)
    # print("   >>> encode2Ascii = ", encode2Ascii)
    result = 0
    if encode2Ascii >= 96: # Lowercase
        result = encode2Ascii - 96
    else: # Uppercase
        result = encode2Ascii - 38
    # print("   >>> result = ", result)
    return result

def findCommonChar(str1, str2):
    result = ''.join(set(str1).intersection(str2))
    return result

def splitStringInHalf(Str2cut):
    # print("  >> Str2cut = ", Str2cut)
    firstStrPart, secondStrPart = Str2cut[:len(Str2cut)//2], Str2cut[len(Str2cut)//2:]
    # print("  >> firstStrPart = ", firstStrPart)
    # print("  >> secondStrPart = ", secondStrPart)
    return firstStrPart, secondStrPart

def checkTwoLargeCompartments(line):
    firstStrPart, secondStrPart = splitStringInHalf(line)
    return firstStrPart, secondStrPart

def checkRucksack(Lines):
    result = 0
    for line in Lines:
        # print(" > line = ", line)
        compartments = checkTwoLargeCompartments(line)
        # print(" > compartments = ", compartments)
        repatingCharacter = findCommonChar(compartments[0], compartments[1])
        # print(" > repatingCharacter = ", repatingCharacter)
        result = result + encodeLetter2Priority(repatingCharacter)
    return result    

def main():
    path2file = './input/input_day03'
    Lines = readFine(path2file)
    Lines = [line.strip() for line in Lines]
    # print("Lines = ", Lines)
    prioritySum = checkRucksack(Lines)
    print("prioritySum = ", prioritySum)

if __name__ == "__main__":
    main()
