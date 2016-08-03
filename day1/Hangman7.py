import random


def guessedAllLetters(secretWord, guessedLetters):
    for i in range(len(secretWord)):
        found = guessedLetters.find(secretWord[i])

        if (found == -1):
            return False
    #
    return True

def printAllIndices(secretWord, letter):
    for i in range(len(secretWord)):
        if (secretWord[i] == letter):
            print(letter + " IS in the secret word at index "
                  + str(i))

def chooseRandomWord(words) :
    rawWordIndex = random.random() * len(words)
    wordIndex = int(rawWordIndex)

    return words[wordIndex]


    # this is the main function, which provides the logic
    # that will be run when this program is executed
if __name__ == "__main__":

    print("Welcome to Hangman!\n")

    with open('hangmanwords.txt', 'r') as f:
        words = f.read().splitlines()

    #words = ["Squirtle", "Totodile", "Mudkip",
             #"Piplup", "Oshawott", "Froakie"]

    #create an array of words via chooseRandomWords(words)
    #assign word to secret word

    secretWord = chooseRandomWord(words)
    secretWord = secretWord.lower()

    incorrect = 0
    allowedIncorrect = 10

    guessedLetters = ""

    print("The length of the secret word: " + str(len(secretWord)))
    print()
    print("You have " + str(allowedIncorrect) + " incorrect guesses.\n")

    while (incorrect < allowedIncorrect):
        letter = input("Enter a letter: ").lower()
        guessedLetters += letter

        indexOfLetter = secretWord.find(letter)

        if (indexOfLetter == -1):
            incorrect += 1
            print(letter + " is NOT in the secret word. ")
            print("That is incorrect guess #" + str(incorrect))
            print()

        else:
            printAllIndices(secretWord, letter)
            print()

            didWin = guessedAllLetters(secretWord, guessedLetters)


            if (didWin):
                break

    if (incorrect < allowedIncorrect):
        print("The secret word was: " + secretWord)
        print("You won! Now go tell someone who actually cares. ")

    else:
        print("The secret word was: " + secretWord)
        print("Sucks to suck. ")