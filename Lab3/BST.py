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
                # Traverse and find leaf
                if data < current.data:
                    previous = current
                    current = previous.left
                else:
                    previous = current
                    current = previous.right
                previous.size += 1
            current = Node.Node(data)
            
            # Create links and variables
            current.depth = previous.depth + 1  # temp
            current.parent = previous
            if data < previous.data:
                previous.left = current
            else:
                previous.right = current
            
            
            #self = self.balanceTree()

        def inOrderWalk(self, leaf : Node):
            list = []
            
            if(leaf.left is not None):
                list += self.inOrderWalk(leaf.left)
            list.append(leaf.data)
            if(leaf.right is not None):
                list += self.inOrderWalk(leaf.right)
            
            return list 
        
        def balanceTree(self):
            list = self.inOrderWalk(self.head)
            balanced = BST()
            
            mid = len(list)//2
            print(list[mid])
            balanced.insert(list[mid])
            for i in range(mid, 0, -1):
                balanced.insert(list[i])
            for i in range(mid+1, len(list)-1):
                balanced.insert(list[i])
        
            return balanced
            
if __name__ == "__main__":
    bst = BST()
    bst.insert(10)
    bst.insert(7)
    bst.insert(4)
    bst.insert(4)
    bst.insert(33)
    bst.insert(9)
    bst.insert(10)
    bst.insert(10)
    bst.insert(72)