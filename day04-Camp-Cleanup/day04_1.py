def readFine(path2file):
    inputFile = open(path2file, 'r')
    Lines = inputFile.readlines()
    return Lines

def isRangesFullyOverlap(line):
    result = 0 
    ranges = line.split(',')
    # print(" > ranges = ", ranges)

    # Build Range1
    rangeStartEnd1 = ranges[0].split('-')
    # print("rangeStartEnd1 = ", rangeStartEnd1)
    range1 = [*range(int(rangeStartEnd1[0]), int(rangeStartEnd1[1]) + 1)]
    # print(" > range1 = ", range1)

    # Build Range2
    rangeStartEnd2 = ranges[1].split('-')
    # print("rangeStartEnd2 = ", rangeStartEnd2)
    range2 = [*range(int(rangeStartEnd2[0]), int(rangeStartEnd2[1]) + 1)]
    # print(" > range2 = ", range2)

    if set(range1).issubset(range2) or set(range2).issubset(range1):
        # print("  >> range1SubsetOfRange2 = ", set(range1).issubset(range2))
        # print("  >> range2SubsetOfRange1 = ", set(range2).issubset(range1))
        result = 1 # range overlap
    return result

def main():
    path2file = './input/input_day04'
    Lines = readFine(path2file)
    Lines = [line.strip() for line in Lines]
    # print("Lines = ", Lines)
    result = 0
    for line in Lines:
        # print("line = ", line)
        result = result + isRangesFullyOverlap(line)

    print("result = ", result)

if __name__ == "__main__":
    main()
