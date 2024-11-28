import random as r
from itertools import accumulate
    
def makeRandomArray(n: int, lowest =-10, highest =10):
    """ Makes an array n long with random ints between lowest and highest """
    return [r.randint(lowest, highest) for _ in range(n)]

def maxSubArray(array, low, high):
    if low == high:
        return{
            'max_sum': array[low],
            'prefix_sum': array[low],
            'suffix_sum': array[low],
            'total_sum': array[low]
        }
    
    mid = (low+high) // 2

    left_result = maxSubArray(array, low, mid)
    right_result = maxSubArray(array, mid+1, high)
    
    total_sum = left_result['total_sum'] + right_result['total_sum']
    prefix_sum = max(left_result['prefix_sum'], left_result['total_sum'] + right_result['prefix_sum'])
    suffix_sum = max(right_result['suffix_sum'], right_result['total_sum'] + left_result['suffix_sum'])
    max_sum = max(left_result['max_sum'], right_result['max_sum'], left_result['suffix_sum'] + right_result['prefix_sum'])


    return {
        'max_sum': max_sum,
        'prefix_sum': prefix_sum,
        'suffix_sum': suffix_sum,
        'total_sum': total_sum
    }

def test(result, array):
    if max(accumulate(array, lambda x, y: max(y, x + y))) == result:
        return True
    return False



if __name__ == '__main__':
    arr = makeRandomArray(10)
    #arr = [7, -5, 2, 6, -1]
    print(arr)
    # Send in index
    res = maxSubArray(arr, 0, len(arr)-1)
    print(res)
    print(test(res, arr))