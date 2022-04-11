class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = set()

    def connect(self, other_node):
        self.neighbors.add(other_node)
        other_node.neighbors.add(self)
    
    def __str__(self):
        return str(self.name)

        
    def __repr__(self):
        return str(self.name)
