
def bubbleSort(arr) :
    for i in range(len(arr) - 1) :
        for j in range(len(arr) - 1 - i) :
            if (arr[j] > arr[j + 1]) :
                swap(arr, j, j + 1)


def swap(arr, index1, index2) :
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

def printArray(arr) :
    if len(arr) > 0 :
        arrStr = str(arr[0])

        for i in range(1, len(arr)):
            arrStr += ", " + str(arr[i])

        print(arrStr, end="")

    print()

if __name__ == "__main__" :

    nums = []

    for i in range(10) :
        nums.append(int(input("Enter a number: ")))

    print("The original values are: ", end="")
    printArray(nums)

    bubbleSort(nums)

    print("The sorted values are: ", end="")
    printArray(nums)


