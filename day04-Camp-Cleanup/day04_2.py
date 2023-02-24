def readFine(path2file):
    inputFile = open(path2file, 'r')
    Lines = inputFile.readlines()
    return Lines

def nrOfRangesWithOverlap(line):
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

    if (len(set(range1).intersection(range2))):
        # anyRangeOverlap = set(range1).intersection(range2)
        # print("  >> anyRangeOverlap = ", anyRangeOverlap)
        # print("  >> len(anyRangeOverlap) = ", len(anyRangeOverlap))
        result = 1 # any range overlap
    return result

def main():
    path2file = './input/input_day04'
    Lines = readFine(path2file)
    Lines = [line.strip() for line in Lines]
    # print("Lines = ", Lines)
    result = 0
    for line in Lines:
        # print("line = ", line)
        result = result + nrOfRangesWithOverlap(line)

    print("result = ", result)

if __name__ == "__main__":
    main()
