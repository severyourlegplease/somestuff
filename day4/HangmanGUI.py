import turtle

class HangmanGUI :
    def __init__(self):
        self.screen = turtle.Screen()
        self.resetScreen()

    # resets the values of the GUI back to start
    def resetScreen(self):
        self.currentBodyPart = 0
        self.image = "../hangman0.gif"

    # doesn't actually display window, but does show an
    # image in it for the first time
    def displayWindow(self) :
        self.resetScreen()
        self.screen.addshape(self.image)
        turtle.shape(self.image)

    # transitions the image to the next appropriate picture
    # ie adds another body part - use when incorrect letter
    # is guessed
    def addBodyPart(self):
        if (self.currentBodyPart < 7) :
            self.currentBodyPart += 1

            self.image = "../hangman" + str(self.currentBodyPart) + ".gif"

            self.screen.addshape(self.image)
            turtle.shape(self.image)

    # to be called IFF someone wins the game
    def winGame(self):
        self.image = "../hangman8.gif"
        self.screen.addshape(self.image)
        turtle.shape(self.image)
