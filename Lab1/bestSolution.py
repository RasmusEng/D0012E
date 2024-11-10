import time
import random
import Stack
import Tests

def SimpleNaive(stack1: Stack, stack2: Stack):
    # Sorts elements from stack1 into stack2 in ascending order
    while not stack1.isEmpty():
        temp = stack1.pop()
        
        while not stack2.isEmpty():
            top = stack2.pop()
            
            if top > temp:
                stack1.push(top)  
            else:
                stack2.push(top)
                break

        stack2.push(temp)
    
    while not stack2.isEmpty():
        stack1.push(stack2.pop())

def main():
    # Just for testing
    stack1 = Stack.Stack()
    stack2 = Stack.Stack()
    
    # Add random integers to stack1
    for i in range(0, 1000):
        stack1.push(random.randint(1,100))
    
    Tests.printStack(stack1) 
    
    start_time = time.time() 
    SimpleNaive(stack1, stack2)
    end_time = time.time()
    
    Tests.printStack(stack1) 
    
    print(Tests.checkSorting(stack1))
    
    execution_time = end_time - start_time 
    print(f"Execution time: {execution_time} seconds") 


if __name__ == "__main__":
    main()