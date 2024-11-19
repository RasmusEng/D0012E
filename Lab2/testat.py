import random as r

def mergeSort(array):
    """ sorts array using mergeSort. Assumes that array is not empty """
    
    # Base case
    if len(array) == 1:
        return array
    
    # Variables
    middle = len(array) // 2
    left = mergeSort(array[:middle])
    right = mergeSort(array[middle:])
    tempArray = []

    # Sorts arrays while merging them
    while len(right) and len(left) != 0:
        if left[0] < right[0]:
            tempArray.append(left.pop(0))
        else:
            tempArray.append(right.pop(0))

    # Readds everything that's left over after sorting
    while len(left) != 0:
        tempArray.append(left.pop(0))
    while len(right) != 0:
        tempArray.append(right.pop(0))

    # Owahhaha
    return tempArray

def makeRandomArray(n: int, lowest =-100000, highest =100000):
    """ Makes an array n long with random ints between lowest and highest """
    return [r.randint(lowest, highest) for _ in range(n)]

if __name__ == '__main__':
    test = makeRandomArray(100000)
    print(mergeSort(test))