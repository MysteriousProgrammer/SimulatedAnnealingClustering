class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def connect(self, other_node):
        self.neighbors.add(other_node)
        other_node.neigjbors.add(self)
