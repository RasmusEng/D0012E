import random as r
    
def makeRandomArray(n: int, lowest =-10, highest =10):
    """ Makes an array n long with random ints between lowest and highest """
    return [r.randint(lowest, highest) for _ in range(n)]

def maxSubSum(array, lower, higher, arrayLength):
    return


def divideAndConquer(array, low, high):
    """ Assumes that array is 1 element or lager """
    if (low > high):
        return -10000
    
    if high == low:
        return array[low]
    
    middle = high+1 // 2
    
    left = divideAndConquer(array, low, middle-1)
    right = divideAndConquer(array, middle+1, high)
    
    return max(left, right)


if __name__ == '__main__':
    # Arr = makeRandomArray(10)
    arr = [7, -5, 2, 6, -1]
    print(arr)
    # Send in index
    print(divideAndConquer(arr, 0, len(arr)-1))