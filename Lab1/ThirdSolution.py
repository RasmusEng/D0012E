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
    
def countStack(stack):
    current = stack.head
    n = 0
    while current:
        current = current.next
        n += 1
    return n
    
def complicatedNaive(stack1):
    n = countStack(stack1)
    tempStack = Stack()
    while (n != 0):
        findLargest(stack1, tempStack, n)
        n-=1

def findLargest(stack1, stack2, n):
    largest = stack1.pop()
    for i in range (1,  n):
        temp = stack1.pop()
        if (temp > largest):
            stack2.push(largest)
            largest = temp
        else:
            stack2.push(temp)
    stack1.push(largest)
    for i in range (1, n):
        stack1.push(stack2.pop())

def printStack(stack):
    elements = []
    current = stack.head
    while current:
        elements.append(current.data)
        current = current.next
    print(" -> ".join(map(str, elements)))

# Main
stack1 = Stack()
    
# Add elements to stack1
stack1.push(1)
stack1.push(1)
stack1.push(3)
stack1.push(8)
stack1.push(4)
stack1.push(5)
stack1.push(23523)
printStack(stack1)
complicatedNaive(stack1)
printStack(stack1)