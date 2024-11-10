import time
import random
class Stack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None
        
    def __init__(self):
        # Constructor for the stack, creates the head of the stack
        self.head = None
    
    def push(self, data):
        # Pushes a new element to the stack
        newNode = self.Node(data)
        newNode.next = self.head
        self.head = newNode
        
    def pop(self):
        # Pop the last element in the stack, returns None if stack is empty
        if self.isEmpty():
            return None
        popedElement = self.head.data
        self.head = self.head.next
        return popedElement
        
    def isEmpty(self):
        # Return true if stack is empty
        return self.head is None



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


def countStack(stack: Stack):
    # Count the elements in the stack
    current = stack.head
    n = 0
    while current:
        current = current.next
        n += 1
    return n


def printStack(stack: Stack):
    # Print out the stack
    elements = []
    current = stack.head
    while current:
        elements.append(current.data)
        current = current.next
    print(" -> ".join(map(str, elements)))
    print("=="*70)


def testStack(stack: Stack):
    # Test if the stack is sorted
    elements = []
    current = stack.head
    while current:
        elements.append(current.data)
        current = current.next
    if elements == sorted(elements):
        return "The stack is sorted"
    return "The stack is NOT sorted"


def main():
    # Just for testing
    stack1 = Stack()
    stack2 = Stack()
    
    # Add random integers to stack1
    for i in range(0, 1000):
        stack1.push(random.randint(1,100))
    
    printStack(stack1) 
    
    start_time = time.time() 
    SimpleNaive(stack1, stack2)
    end_time = time.time()
    
    printStack(stack1) 
    
    print(testStack(stack1))
    
    execution_time = end_time - start_time 
    print(f"Execution time: {execution_time} seconds") 


if __name__ == "__main__":
    main()