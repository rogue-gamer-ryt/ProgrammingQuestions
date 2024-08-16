"""
In this problem, there is an undirected graph with n nodes. There is also an edges array. Where edges[i] = [a,
b] means that there is an edge between node a and node b in the graph.

You need to return the number of connected components in that graph.

Example 1

Input:
3
[[0,1], [0,2]]

Output:
1

Link: https://www.lintcode.com/problem/3651/
"""
from typing import (
    List,
)

class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank  = [1 for _ in range(n)]

        def find(n):
            p = parent[n]

            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1
        res = n
        for n1,n2 in edges:
            res -= union(n1, n2)
        return res