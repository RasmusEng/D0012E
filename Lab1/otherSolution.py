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
        return stack2
    
    n = 0
    found = 0
    smol = stack1.pop()
    n += 1
    while not stack1.isEmpty():
        poped = stack1.pop()
        n += 1
        if poped >= smol:
            stack2.push(smol)
            smol = poped
        else:
            stack2.push(poped)

    stack1.push(smol)
    found += 1
    for z in range(0,n-found):
        stack1.push(stack2.pop())


    while(found <= n):
        steps = 0
        smol = stack1.pop()
        steps += 1
        while steps < n-found:
            poped = stack1.pop()
            steps += 1
            if poped >= smol:
                stack2.push(smol)
                smol = poped
            else:
                stack2.push(poped)
        stack1.push(smol)
        found += 1
        for z in range(0,n-found):
            stack1.push(stack2.pop())
    

def printStack(stack):
    stack2 = Stack()
    while(not stack.isEmpty()):
        element = stack.pop()
        print(element, end=" ")
        stack2.push(element)
    while(not stack2.isEmpty()):
        stack.push(stack2.pop())
    print("")

def main():
    stack1 = Stack()
    stack2 = Stack()
    
    # Add elements to stack1
    for r in range(50):
        stack1.push(random.randint(0,50))

    print("Stack1 before sorting:")
    printStack(stack1)

    # Sort elements in stack1 and place them in stack2
    SimpleNaive(stack1, stack2)
    print("Stack1 after sorting:")
    printStack(stack1)

if __name__ == "__main__":
    main()