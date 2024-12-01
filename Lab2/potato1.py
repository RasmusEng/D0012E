#    MAX = 0
#    LEFT = 1
#    RIGHT = 2
#    TOTAL = 3

def maxiSubbyArray(array, low, high):
    if(low == high):
        return [array[low]] + [array[low]] + [array[low]] + [array[low]]

    mid = (low + high) // 2

    left = maxiSubbyArray(array, low, mid)
    right = maxiSubbyArray(array, mid+1, high)

    left_sum = max(left[1], left[3] + right[1])
    right_sum = max(right[2], right[3] + left[2])
    max_sum = max(left[0], right[0], left[2] + right[1])
    total_sum = left[3] + right[3]

    return [max_sum] + [left_sum] + [right_sum] + [total_sum]
