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
