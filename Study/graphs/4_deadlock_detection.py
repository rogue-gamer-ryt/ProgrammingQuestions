"""
Write a program that takes as input a directed graph and checks if the graph contains a cycle.
"""

class GraphVertex:
    white, gray, black = range(3)

    def __init__(self):
        self.color = GraphVertex.white
        self.edges = []

# Time O(|V| + |E|)
def is_deadlocked(G):
    def has_cycle(curr):
        if curr.color == GraphVertext.gray:
            return True
        
        curr.color = GraphVertex.gray
        if any(next.color !=  GraphVertex.black and has_cycle(next) for next in curr.edges):
            return True
        curr.color = GraphVertex.black
        return False
        

    return any(vertex.color == GraphVertex.white and has_cycle(vertex) for vertext in G)