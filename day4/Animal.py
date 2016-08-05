class Animal :

    def __init__(self, name, species) :
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def setName(self, name):
        self.name = name
