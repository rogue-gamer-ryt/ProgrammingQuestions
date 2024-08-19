"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as
directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it
takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the
signal. If it is impossible for all the n nodes to receive the signal, return -1.


Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Link: https://leetcode.com/problems/network-delay-time/
"""

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        q = [] # minHeap
        adj = collections.defaultdict(list)
        for start, target, time in times:
            adj[start].append((target, time))
        visit = set()
        q = [(0, k)]
        total_time = 0
        while q:
            weight, node = heapq.heappop(q)
            if node in visit:
                continue
            visit.add(node)
            total_time = max(total_time, weight)

            for neighbour, weight2 in adj[node]:
                if neighbour not in visit:
                    heapq.heappush(q, (weight2 + weight, neighbour))
        return total_time if len(visit) == n else -1