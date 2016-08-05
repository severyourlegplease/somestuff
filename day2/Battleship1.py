def readFile(fileName) :
    #[[],[],[],[],[],[],[],[],[],[]];
    board = [[] for i in range(10)]

    infile = open(fileName, 'r').read()

    fileArr = infile.split();

    for i in range(10) :
        for j in range(10) :
            # print("adding" + str(i*10 + j))
            board[i].append(int(fileArr[i*10 + j]))

    return board

def printBoard(gameBoard) :
    print("Here is the current board")
    print()

    for i in range(10) :
        for j in range(10) :
            print(str(gameBoard[i][j]), end=" ")
        print()


if __name__ == '__main__':
    fileName = input("Enter the name of the board configuration file: ")
    print()

    print("Reading configuration file. . .")
    battleBoard = readFile(fileName)
    print()

    printBoard(battleBoard)


