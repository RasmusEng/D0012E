import random as r
    
def makeRandomArray(n: int, lowest =-10, highest =10):
    """ Makes an array n long with random ints between lowest and highest """
    return [r.randint(lowest, highest) for _ in range(n)]

def maxSubSum(array, lower, higher, arrayLength):
    


def divideAndConquer(array, low, higher):
    """ Assumes that array is 1 element or lager """
    if higher == 1:
        return array[0]
    
    middle = higher+1 // 2
    
    left = divideAndConquer(array, low, middle, higher)

    right = divideAndConquer(array, middle, higher higher)


if __name__ == '__main__':
    # Arr = makeRandomArray(10)
    arr = [7, -5, 2, 6, -1]
    print(arr)
    # Send in index
    print(divideAndConquer(arr, 0, len(arr)-1))