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

def findCommonCharFor3Str(str1, str2, str3):
    result = ''.join(set(str1).intersection(str2, str3))
    return result

def checkRucksack(Lines):
    # print(" > Lines = ", Lines)
    # print(" > type(Lines) = ", type(Lines))
    result = 0
    teamLines = []
    
    for line in Lines:
        # print(" > line = ", line)
        if len(teamLines) < 2:
            teamLines.append(line)
            continue
        teamLines.append(line)
        # print(" > teamLines = ", teamLines)
        repatingCharacter = findCommonCharFor3Str(teamLines[0], teamLines[1], teamLines[2])
        # print(" > repatingCharacter = ", repatingCharacter)
        result = result + encodeLetter2Priority(repatingCharacter)
        # Prepare next 3 string to work with
        teamLines = []
        # print(" > teamLines = ", teamLines)
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
