import random

# takes in a string array of month names and returns a string
# as a formatted date is "June 24" or "February 31"
def randomDate(months, days) :
    rawMonthIndex = random.random()*12
    monthIndex = int(rawMonthIndex)

    rawDayIndex = random.random() * 31
    dayIndex = int(rawDayIndex)

    date = months[monthIndex] + " " + str(days[dayIndex])
    return date

def tryAgain() :
    print()


if __name__ == "__main__" :
    months = ["January", "February", "March", "April",
              "May", "June", "July", "August", "September",
              "October", "November", "December"]

    days = []

    for i in range(31) :
        days.append(i + 1)

    print("I will try to guess your birthday. ")
    print()

    guessAgain = True

    while (guessAgain) :
        # month = random.choice(months)
        # day = random.choice(range(1, 31))
        randDate = randomDate(months, days)
        response = input("Is your birthday " + randDate + "?")

        while not(response.lower() == "yes" or response.lower() == "no") :
            print(response.lower() + " is not a valid answer. ")
            response = input("Would you like me to guess again? ")
            print()

        if (response.lower() == "no") :
            guessAgain = False
            print("I apologize.")
            response = input("Would you like me to guess again? ")
            print()
            if (response.lower() == "yes") :
                response = input("Is your birthday " + randDate + "?")

        if (response.lower() == "yes") :
            guessAgain = True
            print("Cool story. Tell someone who cares. ")
            print()
            break







