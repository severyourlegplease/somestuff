from day4.Animal import Animal

if __name__ == '__main__' :

    numOfAnimals = int(input("How many animals in your zoo? "))

    myAnimals = []

    for i in range(numOfAnimals) :
        spec = input("What is the species of this animal? ")
        name = input("What is the name of this " + spec + " ? ")

        a = Animal(name, spec)

        myAnimals.append(a)

    thisAnimal = 0

    while (thisAnimal != -1) :
        thisAnimal = int(input("What is the number (0 through "
                               + str(numOfAnimals - 1)
                               + ", -1 to quit) of the animal do you want to see? "))

        if (thisAnimal != -1) :
            a = myAnimals[thisAnimal]

            print("The animal's name is " + a.getName())
            print("The animal's species is " + a.getSpecies())
            print()

            changeName = input("Would you like to change the animal's name? ")

            if (changeName[0] == "y" or changeName[0] == "Y") :
                newName = input("What would you like the new name to be? ")

                a.setName(newName)
                
    print("Thank you for visiting the zoo! ")
