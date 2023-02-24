def readFine(path2file):
    inputFile = open(path2file, 'r')
    Lines = inputFile.readlines()
    return Lines

def findListMaxSum(Lines):
    maxElf1 = 0
    maxElf2 = 0
    maxElf3 = 0
    currentElfSum = 0

    for line in Lines:
        # print(' > line = ', line)
        if line != '\n':
            currentElfSum = currentElfSum + int(line)
            # print(" > currentElfSum = ", currentElfSum)
        else:
            if currentElfSum >= maxElf1:
                maxElf3 = maxElf2
                maxElf2 = maxElf1
                maxElf1 = currentElfSum
            elif currentElfSum >= maxElf2:
                maxElf3 = maxElf2
                maxElf2 = currentElfSum
            elif currentElfSum >= maxElf3:
                maxElf3 = currentElfSum
            currentElfSum = 0
    
    max3Sum = maxElf1 + maxElf2 + maxElf3
    # print(" > maxElf1 = ", maxElf1)
    # print(" > maxElf2 = ", maxElf2)
    # print(" > maxElf3 = ", maxElf3)
    return max3Sum

def main():
    path2file = './input/input_day01'
    Lines = readFine(path2file)
    Lines = [line.strip() for line in Lines]
    # print("Lines = ", Lines)
    max3Value = findListMaxSum(Lines)
    print("max3Value = ", max3Value)

if __name__ == "__main__":
    main()
