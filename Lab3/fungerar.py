import Node 
from graphviz import Digraph
from random import randint

class BST:
    def __init__(self, C):
        """Constructor for BST"""
        self.head = None
        self.C = C
    
    def isEmpty(self):
        """Return if BST is empty"""
        return self.head is None
    
    def size(self):
        """Return size of BST"""
        return self.head.size +1
    
    def lookUp(self, data, node):
        """Checks if data is in BST"""
        if data == node.data:
            return True
        if data > node.data:
            if node.right == None:
                return False
            return self.lookUp(data, node.right)
        else:
            if node.left == None:
                return False
            return self.lookUp(data, node.left)

    def getBalance(self, node) -> bool:
        """Returns True if BST is balanced according to lab instructions"""
        if node is None:
            return True
    
        left_size  = node.left.size if node.left else 0
        right_size = node.right.size if node.right else 0
        return abs(left_size - right_size) <= self.C

    def checkBalance(self, node): 
        """Check and rebalance the subtree rooted at 'node'."""
        while node:
            if not self.getBalance(node):
                balanced_subtree = self.balanceTree2(node)
                if node == self.head:
                    self.head = balanced_subtree
                else:
                    parent = node.parent
                    if parent.left == node:
                        parent.left = balanced_subtree
                    else:
                        parent.right = balanced_subtree
                    balanced_subtree.parent = parent
            node = node.parent
    
    def insert(self, data): 
        """Inserts new element on correct spot"""
        if self.isEmpty():
            self.head = Node.Node(data)
            return "Inserted"
        if self.lookUp(data, self.head):
            return "Data already exist"
        
        current = self.head
        while current:
            # Traverse and find leaf
            current.size += 1
            if data < current.data:
                if current.left is None:
                    current.left = Node.Node(data)
                    current.left.parent = current
                    self.checkBalance(current)
                    return
                current = current.left
            else: # Dubletter sätts in till höger
                if current.right is None:
                    current.right = Node.Node(data)
                    current.right.parent = current
                    self.checkBalance(current)
                    return
                current = current.right

    def inOrderWalk(self, node : Node):
        """"Uses inorderwalk to create a list representing the tree"""
        list = []
        if node.left:
            list += self.inOrderWalk(node.left)
        list.append(node.data)
        if node.right:
            list += self.inOrderWalk(node.right)
        
        return list
    
    def balanceTree2(self, node):
            """Rebalance the subtree rooted at 'node' using a divide and conquer"""
            elements = self.inOrderWalk(node)

            def build_balanced_tree(start, end):
                if start > end:
                    return None
                mid = (start + end) // 2
                root = Node.Node(elements[mid])
                root.left = build_balanced_tree(start, mid - 1)
                root.right = build_balanced_tree(mid + 1, end)

                left_size = root.left.size if root.left else 0
                right_size = root.right.size if root.right else 0
                if root.left and root.right:
                    root.size = 2 + left_size + right_size
                elif root.left or root.right:
                    root.size = 1 + max(left_size, right_size)
                else:
                    root.size = 0
                if root.left:
                    root.left.parent = root
                if root.right:
                    root.right.parent = root
                return root

            return build_balanced_tree(0, len(elements) - 1)
    
    def display(self):
        """ Generate and render the BST visualization """
        dot = self.create_graph(self.head)
        dot.render('bst_tree', format='png', cleanup=True)

        
            
        def create_graph(self, node):
            """Create a Graphviz object from the BST, treating duplicates as separate nodes."""
            dot = Digraph()
            unique_counter = {}  # To assign unique labels to duplicate nodes

            def add_edges(node):
                if node:
                    # Generate a unique label for the current node
                    unique_label = f"{node.data}_{unique_counter[node]}"
                    dot.node(unique_label, label=f"{node.data} (size={node.size})")

                    if node.left:
                        left_label = f"{node.left.data}_{unique_counter[node.left]}"
                        dot.node(left_label, label=f"{node.left.data} (size={node.left.size})")  # Add the left child node
                        dot.edge(unique_label, left_label)  # Create an edge to the left child
                        add_edges(node.left)

                    if node.right:
                        right_label = f"{node.right.data}_{unique_counter[node.right]}"
                        dot.node(right_label, label=f"{node.right.data} (size={node.right.size})")  # Add the right child node
                        dot.edge(unique_label, right_label)  # Create an edge to the right child
                        add_edges(node.right)

            def assign_unique_labels(node):
                """Assign a unique index to every node for differentiation."""
                if node:
                    unique_counter[node] = unique_counter.get(node, len(unique_counter))
                    assign_unique_labels(node.left)
                    assign_unique_labels(node.right)

            # Assign unique labels to all nodes in the tree
            assign_unique_labels(self.head)
            add_edges(self.head)
            return dot