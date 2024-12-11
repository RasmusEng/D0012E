import Node 
from graphviz import Digraph
from random import randint

class BST:
        def __init__(self):
            self.head = None
        
        def isEmpty(self):
            return self.head is None
        
        def getBalance(self, node):
            """Calculate the balance factor of a node."""
            if node is None:
                return 0
            left_height = node.left.height if node.left else 0
            right_height = node.right.height if node.right else 0
            return left_height - right_height
        
        def isBalanced(self):
            """Returns True if the tree is balanced, False otherwise."""
            def check_balance(node):
                if node is None:
                    return 0
                
                left_height = check_balance(node.left)
                if left_height == -1:  # Left subtree is unbalanced
                    return -1
                
                right_height = check_balance(node.right)
                if right_height == -1:  # Right subtree is unbalanced
                    return -1
                
                balance_factor = self.getBalance(node)
                if abs(balance_factor) > 1:  # Unbalanced node
                    return -1
                
                return max(left_height, right_height) + 1  # Return height

            # Start from the root
            return check_balance(self.head) != -1

        def updateHeight(self, node):
            if node is not None:
                left_height = node.left.height if node.left else 0
                right_height = node.right.height if node.right else 0
                node.height = 1 + max(left_height, right_height)

        def insert(self, data): 
            # Inserts new element on correct spot
            if self.isEmpty():
                self.head = Node.Node(data)
                return
            
            # Normal insert
            previous = None
            current = self.head

            while current:
                # Traverse and find leaf
                previous = current
                if data < current.data:
                    if current.left is None:
                        current.left = Node.Node(data)
                        current.left.parent = current
                        break
                    current = current.left
                else: # Dubletter sätts in till höger
                    if current.right is None:
                        current.right = Node.Node(data)
                        current.right.parent = current
                        break
                    current = current.right
            
            if not self.isBalanced():
                # Collect the nodes in sorted order (in-order traversal)
                balanced_tree= self.balanceTree()
                self.head = balanced_tree.head
            
            """ newNode = Node.Node(data)
            newNode.parent = previous """
            """             
            if data < previous.data:
                previous.left = newNode
            else:
                previous.right = newNode """
            
            node = current
            while node:
                self.updateHeight(node)
                node = node.parent

        def inOrderWalk(self, leaf : Node):
            list = []
            
            if leaf.left:
                list += self.inOrderWalk(leaf.left)
            list.append(leaf.data)
            if leaf.right:
                list += self.inOrderWalk(leaf.right)
            
            return list 
        
        def balanceTree(self):
            list = self.inOrderWalk(self.head)
            balanced = BST()
            
            mid = len(list)//2
            balanced.insert(list[mid])
            # Insert the left part
            for i in range(mid - 1, -1, -1):
                balanced.insert(list[i])

            # Insert the right part
            for i in range(mid + 1, len(list)):
                balanced.insert(list[i])
        
            return balanced
        
        def create_graph(self, node):
            """ Create a graphviz object from the BST, including duplicates """
            dot = Digraph()
        
            def add_edges(node):
                if node:
                    if node.left:
                        dot.node(str(node.left.data))  # Add left child
                        dot.edge(str(node.data), str(node.left.data))  # Create edge
                        add_edges(node.left)
                    if node.right:
                        dot.node(str(node.right.data))  # Add right child
                        dot.edge(str(node.data), str(node.right.data))  # Create edge
                        add_edges(node.right)
            
            dot.node(str(node.data))  # Add root node
            add_edges(node)
            return dot

        def draw_graph(self):
            """ Generate and render the BST visualization """
            dot = self.create_graph(self.head)
            dot.render('bst_tree', format='png', cleanup=True)  # Output as PNG image
        
            
if __name__ == "__main__":
    bst = BST()
    high = 100
    low = -100
    for i in range(1, 20):
        randomInt = randint(low, high)
        bst.insert(randomInt)
    
    bst.draw_graph()
    