import random as r
from itertools import accumulate
    
def makeRandomArray(n: int, lowest =-10, highest =10):
    """ Makes an array n long with random ints between lowest and highest """
    return [r.randint(lowest, highest) for _ in range(n)]

def maxSubCross(array, low, middle, high):
    left_sum = float('-inf')
    sum_left = 0
    for i in range(middle, low - 1, -1):
        sum_left += array[i]
        if sum_left > left_sum:
            left_sum = sum_left

    # Max sum on the right of the midpoint
    right_sum = float('-inf')
    sum_right = 0
    for i in range(middle + 1, high + 1):
        sum_right += array[i]
        if sum_right > right_sum:
            right_sum = sum_right

    return left_sum + right_sum

def divideAndConquer(array, low, high):
    """ Assumes that array is 1 element or lager """
    if (low > high):
        return float('-inf')
    
    if low == high:
        return array[low]
    
    middle = (low + high) // 2
    
    left = divideAndConquer(array, low, middle)
    right = divideAndConquer(array, middle+1, high)
    cross = maxSubCross(array, low, middle, high)

    return max(left, right, cross)

def test(result, array):
    if max(accumulate(array, lambda x, y: max(y, x + y))) == result:
        return True
    return False



if __name__ == '__main__':
    arr = makeRandomArray(10)
    #arr = [7, -5, 2, 6, -1]
    print(arr)
    # Send in index
    res = divideAndConquer(arr, 0, len(arr)-1)
    print(res)
    print(test(res, arr))