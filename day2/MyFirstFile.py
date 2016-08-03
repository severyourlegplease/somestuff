def readingStringFromUser() :
    strs = []

    strs.append(input("Enter string #1: "))
    strs.append(input("Enter string #2: "))
    strs.append(input("Enter string #3: "))

    return strs


def printStrings(strs) :
    for i in range(len(strs)) :
        print("  " + strs[i])

def writeToFile(strs, fileName) :
    outfile = open(fileName, 'w')

    for i in range(len(strs)) :
        outfile.write(strs[i] + "\n")

def readFromFile(fileName) :
    strs = []

    infile = open(fileName, 'r').read()

    for line in infile.splitlines() :
        strs.append(line)

    return strs



if __name__ == "__main__" :
    fileName = input("Enter name of output file: ")
    print()

    userInput = readingStringFromUser()

    print("Here are the values you entered: ")
    printStrings(userInput)
    print()

    print("Writing to " + fileName + ". . .")
    writeToFile(userInput, fileName)

    print("Reading from " + fileName + ". . .")
    fileContents = readFromFile(fileName)
    print()

    print("Here are the values that were in the file: ")
    printStrings(fileContents)