"""
Design an algorithm that takes a set of pins and a set of wires connecting pairs of pins, and
determines if it is possible to place some pins on the left half of a PCB, and the remainder on the
right half, such that each wire is between left and right halves. Retum such a division, if one exists
"""

class GraphVertex:
    def __init__(self):
        self.d = -1
        self.endges = []

def is_any_placement_feasible(G):
    def bfs(s):
        s.d = 0
        q = collections.deque([s])

        while q:
            for t in q[0].edges:
                if t.d == -1:
                    t.d = q[0].d + 1
                    q.append(t)
                elif t.d == q[0].d:
                    return False
            del q[0]
        return True
    return all(bfs(v) for v in G if v.d == -1)