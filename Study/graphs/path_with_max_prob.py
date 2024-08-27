"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [
a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge
succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and
return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer
by at most 1e-5.



Example 1:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2 Output: 0.25000 Explanation:
There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

Link: https://leetcode.com/problems/path-with-maximum-probability/
"""


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        adj = collections.defaultdict(list)
        for i, (u, v) in enumerate(edges):
            adj[u].append((v, succProb[i]))
            adj[v].append((u, succProb[i]))

        max_prob = [0.0] * n
        max_prob[start_node] = 1.0

        pq = [(-1.0, start_node)]
        while pq:
            cur_prob, cur_node = heapq.heappop(pq)
            if cur_node == end_node:
                return -cur_prob

            for nxt_node, path_prob in adj[cur_node]:
                if -cur_prob * path_prob > max_prob[nxt_node]:
                    max_prob[nxt_node] = -cur_prob * path_prob
                    heapq.heappush(pq, (-max_prob[nxt_node], nxt_node))
        return 0.0