import graph
import random

def get_test_graph():
    random.seed(0)
    # This is a hard-coded graph for testing
    a = graph.Node('a')
    b = graph.Node('b')
    c = graph.Node('c')
    d = graph.Node('d')
    e = graph.Node('e')
    f = graph.Node('f')
    g = graph.Node('g')
    h = graph.Node('h')

    a.connect(b)
    a.connect(c)
    b.connect(c)
    c.connect(d)
    d.connect(e)
    e.connect(f)
    f.connect(g)
    f.connect(h)
    g.connect(h)
    
    nodes = [a, b, c, d, e, f, g, h]

    random.shuffle(nodes)

    return nodes

def generate_test():
    random.seed(0)
    nodes = []
    number_of_nodes = 1000
    number_of_neighbors_per_node = 5
    for i in range(0, number_of_nodes):
        nodes.append(graph.Node("n_" + str(i)))
    
    for node in nodes:
        for i in range(0, number_of_neighbors_per_node):
            another_node = random.choice(nodes)
            if node != another_node:
                node.connect(another_node)
    random.shuffle(nodes)

    return nodes
