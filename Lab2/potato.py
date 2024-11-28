import random as r
from itertools import accumulate

from enum import Enum
class Index(Enum):
    MAX = 0
    LEFT = 1
    RIGHT = 2
    TOTAL = 3

def maxiSubbyArrau(array, low, high):
    if(low == high):
        return [array[low]] + [array[low]] + [array[low]] + [array[low]]
    
    mid = (low + high) // 2
    
    left = maxiSubbyArrau(array, low, mid)
    right = maxiSubbyArrau(array, mid+1, high)
    
    left_sum = max(left[Index.LEFT.value], left[Index.TOTAL.value] + right[Index.LEFT.value])
    right_sum = max(right[Index.RIGHT.value], right[Index.TOTAL.value] + left[Index.RIGHT.value])
    max_sum = max(left[Index.MAX.value], right[Index.MAX.value], left[Index.RIGHT.value] + right[Index.LEFT.value])
    total_sum = left[Index.TOTAL.value] + right[Index.TOTAL.value]
    
    return [max_sum] + [left_sum] + [right_sum] + [total_sum]







def makeRandomArray(n: int, lowest =-10, highest =10):
    """ Makes an array n long with random ints between lowest and highest """
    return [r.randint(lowest, highest) for _ in range(n)]

def test(result, array):
    if max(accumulate(array, lambda x, y: max(y, x + y))) == result:
        return True
    return False



if __name__ == '__main__':
    arr = makeRandomArray(100)
    #arr = [7, -5, 2, 6, -1]
    print(arr)
    # Send in index
    res = maxiSubbyArrau(arr, 0, len(arr)-1)
    print(res)
    print(test(res[Index.MAX.value], arr))