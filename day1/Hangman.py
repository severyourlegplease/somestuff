import random
import time
from day4.HangmanGUI import HangmanGUI
from day4.HangmanHelper import HangmanHelper
from day4.HangmanUser import HangmanUser

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
    for i in range(len(arr)) :
        print(arr[i], end=" ")
    print()
        #hiddenWord = '_ ' * len(secretWord)
        #print(hiddenWord, " ", end="")


def updateCorrectGuesses(arr, secretWord, letter) :
    #loop through the array
    for i in range(len(arr)) :
    # if the letter is found in the secretWord
        if (secretWord[i] == letter) :
            arr[i] = letter

    #stick the same letter in the same index

    # this is the main function, which provides the logic
    # that will be run when this program is executed
if __name__ == "__main__" :
    print("Welcome to Hangman!\n")

    # ask user for name
    userName = input("Enter your name: ")
    # create hangmanUser object with name
    hUser = HangmanUser(userName)
    print()
    #greet user by name
    print("Hello " + userName + ". \n")

    #somewhere below where they win or lose, increment the appropriate value in the HangmanUser object.
    gui = HangmanGUI()

    gui.displayWindow()

    #find where to call .addBodyPart()
    #find where to call .winGame
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
    allowedIncorrect = 7

    guessedLetters = ""

    print("The length of the secret word: " + str(len(secretWord)))
    print()
    print("You have " + str(allowedIncorrect) + " incorrect guesses.\n\n")

    haveBeenGuessed = []

    for i in range(256) :
        haveBeenGuessed.append(False)

    hHelp = HangmanHelper(haveBeenGuessed)

    while (incorrect < allowedIncorrect):
        printCorrectSoFar(correctSoFar)
        print("Letters so far: " + hHelp.getGuessedLetters(), end="")
        print()

        letter = input("Enter a letter: \n").lower()
        guessedLetters += letter


        indexOfLetter = secretWord.find(letter)

        if (hHelp.hasCharBeenGuessed(letter)) :
            print("You already guessed the letter " + letter + ". Try again. \n")

        elif (indexOfLetter == -1):
            incorrect += 1
            print(letter + " is NOT in the secret word. ")
            print("That is incorrect guess #" + str(incorrect))
            print()

            gui.addBodyPart()



        else:
            #update correctSoFar
            updateCorrectGuesses(correctSoFar, secretWord, letter)
            printAllIndices(secretWord, letter)
            print()

            didWin = guessedAllLetters(secretWord, guessedLetters)


            if (didWin):
                break

        hHelp.charguessed(letter)

    print("The secret word was: " + secretWord)


    if (incorrect < allowedIncorrect):
        print("You won! Now go tell someone who actually cares. ")
        gui.winGame()

        hUser = HangmanUser()
    else:
        print("Sucks to suck. ")

    time.sleep(5)