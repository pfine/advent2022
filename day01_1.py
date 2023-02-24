def readFine(path2file):
    inputFile = open(path2file, 'r')
    Lines = inputFile.readlines()
    return Lines

def findListMaxSum(Lines):
    maxSum = 0
    currentElfSum = 0

    for line in Lines:
        # print(' > line = ', line)
        if line != '\n':
            currentElfSum = currentElfSum + int(line)
            # print(" > currentElfSum = ", currentElfSum)
        else:
            if currentElfSum > maxSum:
                maxSum = currentElfSum
            currentElfSum = 0
    
    # print(" > maxSum = ", maxSum)
    return maxSum

def main():
    path2file = './input/input_day01'
    Lines = readFine(path2file)
    Lines = [line.strip() for line in Lines]
    # print("Lines = ", Lines)
    maxValue = findListMaxSum(Lines)
    print("maxValue = ", maxValue)

if __name__ == "__main__":
    main()
