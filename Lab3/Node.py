class Node:
        def __init__(self, data):
            # Constructor for node, sets variables of node
            self.data = data
            self.height = 0 # temp
            self.depth = 0  # temp
            self.size = 1
            self.left = None
            self.right = None
            self.parent = None