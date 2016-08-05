from day4.User import User

class HangmanUser(User) :

    def __init__(self, name,):
        super(HangmanUser, self).__init__(name)
        self.numWins = 0
        self.numLosses = 0

        # 2 fields, numWins, numLosses, initialize them both to 0

    def getNumWins(self) :
        #return number of wins
        return self.numWins

    def incrementWins(self):
        #add 1 to the number of wins stored in this object
        self.numWins += 1

    def getNumLosses(self):
        #return number of loses
        return self.numLosses

    def incrementNumLosses(self):
        #add 1 to the number of losses stored in this object
        self.numLosses += 1

        #wins is an integer
    def setNumWins(self, wins):
        #change numbers of wins stored in this object to wins
        self.numWins = wins

    def setNumLosses(self, losses):
        #change numbers of losses stored in this object to losses
        self.numLosses = losses
