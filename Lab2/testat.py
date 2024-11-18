import random as r

def mergeSort(array):
    """ Assumes that array is 1 element or lager """
    # Returns sorted 2 array
    if len(array) == 1:
        return array
    if len(array) == 2:
        return [array[0], array[1]] if array[0] < array[1] else [array[1], array[0]]
    
    middle = len(array) // 2
    left = mergeSort(array[:middle])
    right = mergeSort(array[middle:])
    temp = []
    while len(right) and len(left) != 0:
        if left[0] < right[0]:
            temp.append(left.pop(0))
        else:
            temp.append(right.pop(0))
    while len(left) != 0:
        temp.append(left.pop(0))
    while len(right) != 0:
        temp.append(right.pop(0))
    return temp

# Oläslighet            

def makeRandomArray(n: int, lowest =-100000, highest =10000):
    """ Makes an array n long with random ints between lowest and highest """
    return [r.randint(lowest, highest) for _ in range(n)]

if __name__ == '__main__':
    test = makeRandomArray(10)
    print(mergeSort(test))