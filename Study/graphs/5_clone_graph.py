"""
Consider a vertex type for a directed graph in which there are two fields: an integer label and a list
of references to other vertices. Design an algorithm that takes a reference to a vertex u, arrd creates
a copy of the graph on the vertices reachable from z. Retum the copy of u.
"""

class GraphVertex:
    def __init__(self, label):
        self.label = label
        self.edges = []

def clone_graph(G):
    if not G:
        return None
    q = collections.deque([G])
    vertex_map = {
        G: GraphVertex(G.label)
    }
    while q:
        v = q.popleft()
        for e in v.edges:
            if e not in vertex_map:
                vertex_map[e] = GraphVertex(e.label)
                q.append(e)
            vertex_map[v].edges.append(vertex_map[e])
    return vertex_map[G]