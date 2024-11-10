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