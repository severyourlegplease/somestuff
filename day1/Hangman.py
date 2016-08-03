import random
import some other junk


def guessedAllLetters(secretWord, guessedLetters):
        found = guessedLetters.find(secretWord[i])

        if (found == -1):
            return False
    #
    return True

def printAllIndices(secretWord, letter):
    for i in range(len(secretWord)):
            print(letter + " IS in the secret word at index "
                  + str(i))

def chooseRandomWord(words) :
    rawWordIndex = random.random() * len(words)
    wordIndex = int(rawWordIndex)

    return words[wordIndex]


    # this is the main function, which provides the logic
    # that will be run when this program is executed
if __name__ == "__main__":
    print("Welcome to Hangman!")

    words = ["Squirtle", "Totodile", "Mudkip",
             "Piplup", "Oshawott", "Froakie"]

    #create an array of words via chooseRandomWords(words)
    #assign word to secret word

    secretWord = chooseRandomWord(words)
    secretWord = secretWord.lower()
    print("Length of secret word: " + str(len(secretWord)))
    print()

    incorrect = 0

    guessedLetters = ""

    print("The length of the secret word: " + str(len(secretWord)))
    print()

    while (incorrect < 7):
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

    if (incorrect < 7):
        print("Good job, you didn't die. ")

    else:
        print("Sucks to suck. ")

