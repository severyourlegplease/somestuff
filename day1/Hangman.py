import random

def guessedAllLetters(secretWord, guessedLetters):
    for i in range(len(secretWord)):
        found = guessedLetters.find(secretWord[i])

        if (found == -1):
            return False

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

def retrieveWords() :
    words = []
    with open('hangmanwords.txt', 'r') as f:
        words = f.read().splitlines()

    return words

def printCorrectSoFar(arr) :
    print("Word: ", end="")
    #loop through the array and print each character followed by a space
    for i in range(len(secretWord)) :
        if (arr == secretWord[i]) :
            print(arr, " ", end="")
        else:
            print("_ ", end="")
        #hiddenWord = '_ ' * len(secretWord)
        #print(hiddenWord, " ", end="")



def updateCorrectGuesses(arr, secretWord, letter) :
    #loop through the array
    for i in range(len(secretWord)) :
    # if the letter is found in the secretWord
        if (secretWord[i] == letter) :
            print()

    #stick the same letter in the same index

    # this is the main function, which provides the logic
    # that will be run when this program is executed
if __name__ == "__main__" :
    print("Welcome to Hangman!\n")

    words = retrieveWords();


    #words = ["Squirtle", "Totodile", "Mudkip",
             #"Piplup", "Oshawott", "Froakie"]

    #create an array of words via chooseRandomWords(words)
    #assign word to secret word

    secretWord = chooseRandomWord(words)
    secretWord = secretWord.lower()

    correctSoFar = []

    for i in range(len(secretWord)) :
        correctSoFar.append('_')

    incorrect = 0
    allowedIncorrect = 10

    guessedLetters = ""

    print("The length of the secret word: " + str(len(secretWord)))
    print()
    print("You have " + str(allowedIncorrect) + " incorrect guesses.\n\n")

    while (incorrect < allowedIncorrect):
        printCorrectSoFar(secretWord)
        print()
        print()
        letter = input("Enter a letter: ").lower()
        guessedLetters += letter

        indexOfLetter = secretWord.find(letter)

        if (indexOfLetter == -1):
            incorrect += 1
            print(letter + " is NOT in the secret word. ")
            print("That is incorrect guess #" + str(incorrect))
            print()

        else:
            #update correctSoFar
            updateCorrectGuesses(correctSoFar, secretWord, letter)
            printAllIndices(secretWord, letter)
            print()

            didWin = guessedAllLetters(secretWord, guessedLetters)


            if (didWin):
                break

    print("The secret word was: " + secretWord)

    if (incorrect < allowedIncorrect):
        print("You won! Now go tell someone who actually cares. ")

    else:
        print("Sucks to suck. ")
