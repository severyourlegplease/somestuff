def readFile(fileName) :
    # board = [[],[],[],[],[],[],[],[],[],[]];
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

def printEncodedBoard(gameBoard) :
    print("Current Board:")

    print("  0 1 2 3 4 5 6 7 8 9")
    for i in range(10) :
        print(str(i), end=" ")

        for j in range(10) :
            actualState = gameBoard[i][j]
            userState = "O"

            if (actualState == 2) :
                userState = "X"
            elif (actualState == 3) :
                userState = "*"

            print(userState, end = " ")

        print()

    print()

def attackAttempt(board, row, column) :
    attackSpot = board[row][column]

    if (attackSpot == 0) :
        print("You missed!")

        board[row][column] = 2
    elif (attackSpot == 1) :
        print("You hit a ship!")

        board[row][column] = 3
    else :
        print("Already attacked here!")

    print()


if __name__ == '__main__':
    fileName = input("Enter the name of the board configuration file: ")
    print()

    print("Reading configuration file. . .")
    battleBoard = readFile(fileName)
    print()

    # printBoard(battleBoard)

    playing = True
    while (playing) :
        printEncodedBoard(battleBoard)
        print()

        row = int(input("Enter row number: "))
        column = int(input("Enter column number: "))

        attackAttempt(battleBoard, row, column)
        print()

