class HangmanHelper :

    def __init__(self, letters) :
        self.letters = letters

    def getGuessedLetters(self):
        options = ""

        for i in range(97, 123):
            if (self.letters[i]) :
                options += "* "

            else :
                options += chr(i) + " "




        return options

    def charguessed(self, letter):
        self.letters[ord(letter)] = True

    def hasCharBeenGuessed(self, letter):
        return self.letters[ord(letter)]
