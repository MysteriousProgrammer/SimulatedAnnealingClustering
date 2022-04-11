import gc
import graph

def get_test_graph():
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

    return nodes
