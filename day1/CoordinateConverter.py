import math


def findRadius(x, y):
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))


def findTheta(x, y):
    radians = math.atan(y / x)
    return math.degrees(radians)


def findX(r, theta):
    return r * math.cos(math.radians(theta))


def findY(r, theta):
    return r * math.sin(math.radians(theta))


def cartesianToPolar(n, x, y):
    print("(x" + n + ", y" + n + ") = (" + str(x) + ", "
          + str(y) + ")    (r" + n + ", theta" + n
          + ") = (" + '{0:.2f}'.format(findRadius(x, y)) + ", "
          + '{0:.2f}'.format(findTheta(x, y)) + ")")


def polarToCartesian(n, r, theta):
    print("(r" + n + ", theta" + n + ") = (" + str(r) + ", "
          + str(theta) + ")    (x" + n + ", y" + n
          + ") = (" + '{0:.2f}'.format(findX(r, theta)) + ", "
          + '{0:.2f}'.format(findY(r, theta)) + ")")

def distance(x1, y1, x2, y2) :
    xSquared = math.pow(x2 - x1, 2)
    ySquared = math.pow(y2 - y1, 2)

    result = math.sqrt(xSquared + ySquared)

    return result;


if __name__ == '__main__':

    askAgain = True

    print("Welcome to the coordinate converter and distance finder")
    print()

    while (askAgain):

        print("c) Cartesian")
        print("p) Polar")
        coordSpace = input("Which coordinate space would you like to use? ").lower()
        print()

        while not (coordSpace == "c" or coordSpace == "p"):
            print(coordSpace + " is not a valid option. Please select a valid option.")
            coordSpace = input("Which coordinate space would you like to use? ")
            print()

        # so that these variables persist after the if/else block
        x1 = x2 = y1 = y2 = 0
        if (coordSpace == "c"):
            print("Cartesian coordinate space selected.")
            print()

            x1 = float(input("Please enter x1: "))
            y1 = float(input("Please enter y1: "))
            x2 = float(input("Please enter x2: "))
            y2 = float(input("Please enter y2: "))
            print()

            cartesianToPolar("1", x1, y1)
            cartesianToPolar("2", x2, y2)

        else :
            print("Polar coordinate space selected.")
            print()

            r1 = float(input("Please enter r1: "))
            theta1 = float(input("Please enter theta1: "))
            r2 = float(input("Please enter r2: "))
            theta2 = float(input("Please enter theta2: "))
            print()

            x1 = findX(r1, theta1)
            y1 = findY(r1, theta1)

            x2 = findX(r2, theta2)
            y2 = findY(r2, theta2)

            polarToCartesian("1", r1, theta1)
            polarToCartesian("2", r2, theta2)

        print()

        print("The distance between the two points is " + '{0:.2g}'.format(distance(x1, y1, x2, y2)))
        print()

        response = input("Would you like to convert more coordinates? ").lower()
        print()

        while not (response == "yes" or response == "no") :
            print(response + " is not a valid response")
            response = input("Would you like to convert more coordinates? ")
            print()

        if (response == "no") :
            askAgain = False

    print("Thank you for using my coordinate converter and distance program.")