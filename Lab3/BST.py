import Node

class BST:
        def __init__(self):
            self.head = None

        def isEmpty(self):
            return self.head is None
        
        def insert(self, data): # Inserts new element on correct spot
            # If empty
            if self.isEmpty():
                self.head = Node.Node(data)
                return

            # Normal insert
            previous = None
            current = self.head
            while current != None:

                # Increase size if duplicates
                if data == current.data:
                    current.size += 1
                    return
                
                # Traverse and find leaf
                if data < current.data:
                    previous = current
                    current = previous.left
                else:
                    previous = current
                    current = previous.right
            current = Node.Node(data)

            # Create links
            current.parent = previous
            if data < previous.data:
                previous.left = current
            else:
                previous.right = current

if __name__ == "__main__":
    bst = BST()
    bst.insert(10)
    bst.insert(7)
    bst.insert(4)
    bst.insert(33)
    bst.insert(9)
    bst.insert(10)
    bst.insert(10)
    bst.insert(72)