import Node 

class BST:
        def __init__(self):
            self.head = None
        
        def isEmpty(self):
            return self.head is None
        
        def getBalance(self, node):
            """ Vi behöver denna för att kunna veta om vet behöver balansera, skulle behövas skrivas om lite """
            if node is None:
                return 0
            return self.node.left.height - self.node.right.height
        
        """ En funktion som uppdaterar height på alla påverkade noder efter vi har balanserat trädet """

        def rotateRight(self, node):
            """ Roterar trädet åt höger, ändra variabelnamnen """
            y = node.left
            temp = y.right
            
            y.right = node
            node.left = temp
            
            """ Uppdatera höjden på noderna y och node """
            
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = y
                else:
                    node.parent.right = y            
            y.parent = node.parent
            node.parent = y
            if temp:
                temp.parent = node
                
            return y
        
        def rotateLeft(self, node):
            """ Roterar trädet åt vänster samma som höger fast bytt plats på left och right, ändra variabelnamnen"""
            y = node.right
            temp = y.left
            
            y.left = node
            node.right = temp
            
            """ Uppdatera höjden på noderna y och node """
            
            if node.parent:
                if node.parent.right == node:
                    node.parent.right = y
                else:
                    node.parent.left = y            
            y.parent = node.parent
            node.parent = y
            if temp:
                temp.parent = node
                
            return y


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
            
            current.depth = previous.depth + 1  # Adds dept
            
            # Create links and variables
            current.parent = previous
            if data < previous.data:
                previous.left = current
            else:
                previous.right = current
            
            leaf = current
            while leaf:
                """ Behöver uppdatera height här """
                self.partialRebalance(leaf)
                leaf = leaf.parent

        def partialRebalance(self, node):
            balance = self.getBalance(node)
            
            """ Om trädet är vänster tungt """
            if balance >= 2:
                if self.getBalance(node.left) < 0:
                    node.left = self.rotateLeft(node.left)
                return self.rotateRight(node)
                    
            """ Om trädet är höger tungt """
            if balance <= -2:
                if self.getBalance(node.right) < 0:
                    node.right = self.rotateLeft(node.right)
                return self.rotateLeft(node)
            
            """ Om trädet redan är balanserat """
            return node
        
        
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