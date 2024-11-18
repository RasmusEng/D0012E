import solution1

def sortR(array):
    length = len(array)
    if length<=4:
        for i in range(0, len(array)-1):
            if array[i] > array[i+1]:
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
    else:
        arraySorted = []
        mid = length // 4
        
        
        print(array[0:mid])
        print(array[mid:mid*2])
        print(array[mid*2:mid*3])
        print(array[mid*3:length])
        
        
        lowerLeft = sortR(array[0:mid])
        lowerRight = sortR(lowerLeft+array[mid:mid*2])
        upperLeft = sortR(array[mid*2:mid*3])
        upperRight = sortR(array[mid*3:length])
        
        print("---------------")
        print(lowerLeft)
        print(lowerRight)
        print(upperLeft)
        print(upperRight)
        print("---------------")
        
        
        
        
        return arraySorted


    return array
            

    


if __name__ == '__main__':
    arr = solution1.makeRandomArray(9)
    #arr = [7, -5, 2, 6]
    print(arr)
    print(sortR(arr))
