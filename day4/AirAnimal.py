from day4.Animal import Animal

class AirAnimal(Animal) :
    def __init__(self, name, species):
        super(AirAnimal, self.__init__(name, species))
        self.wingSpan = 0

    def setWingSpan(self, span):
        self.wingSpan = span

    def getWingSpan(self):
        return self.wingSpan