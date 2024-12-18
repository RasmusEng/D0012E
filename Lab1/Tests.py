import Stack
import SortAlgo

#Just for testing
import time
import random

def printStack(stack: Stack):
    # Print out the stack
    elements = []
    current = stack.head
    while current:
        elements.append(current.data)
        current = current.next
    print(" -> ".join(map(str, elements)))
    print("=="*70)

def checkSorting(stack: Stack):
    # Test if the stack is sorted
    elements = []
    current = stack.head
    while current:
        elements.append(current.data)
        current = current.next
    if elements == sorted(elements):
        return "The stack is sorted"
    return "The stack is NOT sorted"

def runTest(stack1, stack2):
    # Runs the algorithm and checks if it works and how long it takes
    start_time = time.time() 
    SortAlgo.Sort(stack1, stack2)
    end_time = time.time()
    print(checkSorting(stack2))

    execution_time = end_time - start_time 
    print(f"Execution time: {execution_time} seconds") 

def testBestCase(size):
    # Generates test data for the best case of size: size
    stack1 = Stack.Stack()
    stack2 = Stack.Stack()
    for i in range(1, size+1):
        stack1.push(i)

    runTest(stack1, stack2) 
    
def testWorstCase(size):
    # Generates test data for the worst case of size: size
    stack1 = Stack.Stack()
    stack2 = Stack.Stack()
    for i in range(0, size):
        stack1.push(size-i)

    runTest(stack1, stack2)

def testRandom(size):
    # Generates test data with random numbers of size: size
    stack1 = Stack.Stack()
    stack2 = Stack.Stack()
    for i in range(0, size):
        stack1.push(random.randint(1,size))

    runTest(stack1, stack2)

def main():
    # Runs tests
    size = 10000
    
    print("Best case")
    testBestCase(size)
    print()
    
    print("Worst case")
    testWorstCase(size)
    print()
    
    print("Random case")
    testRandom(size)
    print()

if __name__ == "__main__":
    main()