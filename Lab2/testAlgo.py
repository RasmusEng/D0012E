import random as r
from itertools import accumulate
import time

import solution1 as s1
import potato as s2
import potato1 as s25
import rasmustest as s3

def makeRandomArray(n: int, lowest =-10, highest =10):
    """ Makes an array n long with random ints between lowest and highest """
    return [r.randint(lowest, highest) for _ in range(n)]

def test(result, array):
    if max(accumulate(array, lambda x, y: max(y, x + y))) == result:
        return True
    return False

def main():
    arr = makeRandomArray(100000)
    # Send in index
    start_time = time.time()
    res = s1.divideAndConquer(arr, 0, len(arr)-1)
    end_time = time.time()
    print(end_time - start_time)
    print(test(res, arr))

    start_time = time.time()
    res = s2.maxiSubbyArrau(arr, 0, len(arr)-1)
    end_time = time.time()
    print(end_time - start_time)
    print(test(res[0], arr))

    start_time = time.time()
    res = s25.maxiSubbyArray(arr, 0, len(arr)-1)
    end_time = time.time()
    print(end_time - start_time)
    print(test(res[0], arr))

    start_time = time.time()
    res = s3.maxSubArray(arr, 0, len(arr)-1)
    end_time = time.time()
    print(end_time - start_time)

    print(test(res["max_sum"], arr))


if __name__ == '__main__':
    main()
