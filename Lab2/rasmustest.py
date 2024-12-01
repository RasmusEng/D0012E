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
