import time

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
        return stack2
    
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

def printStack(stack):
    # Print out the stack
    elements = []
    current = stack.head
    while current:
        elements.append(current.data)
        current = current.next
    print(" -> ".join(map(str, elements)))
        
def countStack(stack):
    # Count the elements in the stack
    current = stack.head
    n = 0
    while current:
        current = current.next
        n += 1
    return n

def main():
    stack1 = Stack()
    stack2 = Stack()
    
    # Add elements to stack1
    stack1.push(1)
    stack1.push(1321)
    stack1.push(3)
    stack1.push(8)
    stack1.push(4)
    stack1.push(5)
    stack1.push(52)
    stack1.push(565)
    stack1.push(565)
    stack1.push(10)
    
    start_time = time.time() 
    for i in range(countStack(stack1)):
        SimpleNaive(stack1, stack2)
        print("Stack2 after sorting:", i)
        printStack(stack1)
        printStack(stack2)
    end_time = time.time() 
    execution_time = end_time - start_time 
    print(f"Execution time: {execution_time} seconds") 
if __name__ == "__main__":
    main()