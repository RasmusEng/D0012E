import random as r


def main():
    for i in range(4, 100004, 1000):    
        arr = makeRandomArray(i)
        # import the solution for sorting
        checkIfSorted(arr, i)

def makeRandomArray(n: int, lowest =-100, highest =100):
    """ Makes an array n long with random ints between lowest and highest """
    return [r.randint(lowest, highest) for _ in range(n)]

def checkIfSorted(arr, n):
    if arr == sorted(arr):
        print("Sorterad array med {}st element", n)
        return True
    print("Arrayen är inte sorterad")
    return False




if __name__ == '__main__':
    main()