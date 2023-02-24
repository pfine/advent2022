def readFine(path2file):
    inputFile = open(path2file, 'r')
    Lines = inputFile.readlines()
    return Lines

def main():
    path2file = './input/input_day08_exp1'
    Lines = readFine(path2file)
    Lines = [line.strip() for line in Lines]
    print("Lines = ", Lines)

    for line in Lines:
        print(" > line = ", line)

    print("Hello World!")

if __name__ == "__main__":
    main()
