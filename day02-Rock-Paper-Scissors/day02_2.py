def readFine(path2file):
    inputFile = open(path2file, 'r')
    Lines = inputFile.readlines()
    return Lines

def oponentMove(char1):
    # The first column is what your opponent is going to play: 
        # - A for Rock, (1)
        # - B for Paper, and (2) 
        # - C for Scissors (3)
    # print('  >> char1 = ', char1)
    if char1 == 'A':
        return 1
    elif char1 == 'B':
        return 2
    return 3

def yourMove(char3, oponentMove):
    # The second column says how the round needs to end: 
        # - X means you need to lose, 
        # - Y means you need to end the round in a draw, and 
        # - Z means you need to win
    # print('  >> char3 = ', char3)
    if char3 == 'X': # LOST
        if oponentMove == 1:
            return 3
        elif oponentMove == 2: 
            return 1
        return 2
    elif char3 == 'Y': # DRAW
        return oponentMove
    # WIN
    if oponentMove == 1:
        return 2
    elif oponentMove == 2: 
        return 3
    return 1

def roundResult(line):
    # Your total score is the sum of your scores for each round. 
        # The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
        #   plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
    oponent = oponentMove(line[0])
    my = yourMove(line[2], oponentMove)
    result = my
    if my == oponent: # draw
        # print("  >> result = ", result + 3, ' - DRAW')
        return result + 3
    elif (my == 1 and oponent == 2) or (my == 2 and oponent == 3) or (my == 3 and oponent == 1): # lost
        # print("  >> result = ", result , ' - LOST')
        return result 
    # win
    # print("  >> result = ", result + 6, ' - WIN')
    return result + 6

def gameReult(Lines):
    result = 0

    for line in Lines:
        # print(" > line = ", line)
        result = result + roundResult(line)

    # print(" > result = ", result)
    return result    

def main():
    path2file = './input/input_day02'
    Lines = readFine(path2file)
    Lines = [line.strip() for line in Lines]
    result = gameReult(Lines)
    print("result = ", result)

if __name__ == "__main__":
    main()
