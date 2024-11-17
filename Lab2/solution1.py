import random as r
    
def makeRandomArray(n: int, lowest =-10, highest =10):
    """ Makes an array n long with random ints between lowest and highest """
    return [r.randint(lowest, highest) for _ in range(n)]

def divideAndConquer(array, max = None):
    arrayLength = len(array)
    """ Assumes that array is 1 element or lager """
    if arrayLength == 1:
        return array[0]
    
    middle = arrayLength // 2
    print(array[:middle])
    left = divideAndConquer(array[:middle])
    print(array[middle:])
    right = divideAndConquer(array[middle:])

    if left + right >= left or right:
        return left + right
    else:
        return left if left > right else right


if __name__ == '__main__':
    #arr = makeRandomArray(10)
    arr = [7, -5, 2, 6, -1]
    print(arr)
    print(divideAndConquer(arr))