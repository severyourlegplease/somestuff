import random

def rollSingleDie() :
    rawRoll = 6 * random.random() + 1

    roll = int(rawRoll)

    return roll

def printResults(rolls) :
    for i in range(2, 13) :
        print(str(i) + ": ", end="")
        for j in range(rolls[i]) :
            print("X", end="")

        print(" " + str(rolls[i]))


if __name__ == "__main__" :

    timesRolled = []

    for i in range(13) :
         timesRolled.append(0)

    numberOfRolls = int(input("How many rolls of the dice do you want? "))

    for i in range(numberOfRolls) :
        roll1 = rollSingleDie()
        roll2 = rollSingleDie()

        total = roll1 + roll2

        timesRolled[total] += 1

    printResults(timesRolled)