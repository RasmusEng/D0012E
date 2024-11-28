import random as r
from itertools import accumulate
    
def makeRandomArray(n: int, lowest =-10, highest =10):
    """ Makes an array n long with random ints between lowest and highest """
    return [r.randint(lowest, highest) for _ in range(n)]



def divideAndConquer(array,beginLeftIndex, beginRightIndex):
    if len(array) == 0:
        return float('-inf'), 0, 0
    if len(array) == 1:
        return array[0], beginLeftIndex, beginRightIndex
    
    middle = len(array) // 2
    beginLeftIndex += 0
    beginRightIndex += middle
    leftMax, beginLeftIndex, endLeftIndex = divideAndConquer(array[:middle], beginLeftIndex,0)
    rightMax, beginRightIndex, endRightIndex= divideAndConquer(array[middle:], beginRightIndex,0)
    print("POTATIS")
    
    sum = float('-inf')
    if(isinstance(leftMax, int) and isinstance(rightMax,int)):
        sum = leftMax + rightMax
        for i in range(endLeftIndex+1, beginRightIndex):
            sum += array[i]
    
    maxi = max(sum, leftMax, rightMax)
    if(maxi == sum):
        return sum, beginLeftIndex, endRightIndex
    elif(maxi == leftMax):
        return leftMax, beginLeftIndex, endLeftIndex
    else:  
        returnLeft = beginRightIndex
        returnRight = endRightIndex
        return rightMax, returnLeft, returnRight

def test(result, array):
    if max(accumulate(array, lambda x, y: max(y, x + y))) == result:
        return True
    return False

if __name__ == '__main__':
    #arr = makeRandomArray(10)
    arr = [7, -5, 2, 6, -1, 2]
    print(arr)
    # Send in index
    res = divideAndConquer(arr,0,0)
    print(res)
    print(arr)
    print(test(res[0], arr))