import time
import random
class Stack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
        
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
    
def SimpleNaive(stack1, stack2):
    if stack1.isEmpty():
        return stack1
    
    pushed = 0
    bog = stack1.pop()
    while not stack1.isEmpty():
        poped = stack1.pop()
        if poped >= bog:
            stack2.push(bog)
            bog = poped
        else:
            stack2.push(poped)
        pushed += 1
    stack1.push(bog)

    for i in range(pushed):
        temp = stack2.pop()
        stack1.push(temp)
        
def countStack(stack):
    # Count the elements in the stack
    current = stack.head
    n = 0
    while current:
        current = current.next
        n += 1
    return n

def startSort(stack1, stack2):
    # Start the sorting
    for i in range(countStack(stack1)):
        SimpleNaive(stack1, stack2)
        
def printStack(stack):
    # Print out the stack
    elements = []
    current = stack.head
    while current:
        elements.append(current.data)
        current = current.next
    print(" -> ".join(map(str, elements)))
    print("-"*100)
        
def testStack(stack):
    # Test if the stack is sorted
    elements = []
    current = stack.head
    while current:
        elements.append(current.data)
        current = current.next
    if elements == sorted(elements):
        return True
    return False

def main():
    # Just for testing
    stack1 = Stack()
    stack2 = Stack()
    
    # Add elements to stack1
    for i in range(0, 10000):
        stack1.push(random.randint(1,100000))
    
    printStack(stack1)
    
    start_time = time.time() 
    startSort(stack1, stack2)
    end_time = time.time()
    
    printStack(stack1) 
    
    print(testStack(stack1))
    
    execution_time = end_time - start_time 
    print(f"Execution time: {execution_time} seconds") 


if __name__ == "__main__":
    main()