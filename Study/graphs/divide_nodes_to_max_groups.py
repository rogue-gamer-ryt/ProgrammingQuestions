"""
You are given a positive integer n representing the number of nodes in an undirected graph. 
The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that 
there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group 
with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. 
Return -1 if it is impossible to group the nodes with the given conditions.

 
Example 1:


Input: n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
Output: 4
Explanation: As shown in the image we:
- Add node 5 to the first group.
- Add node 1 to the second group.
- Add nodes 2 and 4 to the third group.
- Add nodes 3 and 6 to the fourth group.
We can see that every edge is satisfied.
It can be shown that that if we create a fifth group and move any node from the third or fourth group to it, at least on of the edges will not be satisfied.

Link: https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/
"""

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Nodes in a group cannot be connected to each other
        # All the nodes in a group could be connected to only group -1 and group + 1
        adj = defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def get_connected_component(src):
            component = set([src])
            q = deque([src])
            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if nei in component:
                        continue
                    q.append(nei)
                    component.add(nei)
                    visit.add(nei)
            return component

        def get_longest_path(src):
            q = deque([(src, 1)]) # node, group_id
            dist = {src : 1}
            while q:
                node, length = q.popleft()
                for nei in adj[node]:
                    if nei in dist:
                        if dist[nei] not in (length  + 1, length - 1):
                            return -1
                        continue
                    q.append((nei, length + 1))
                    dist[nei] = length + 1
            return max(dist.values())

        
        visit = set()

        res = 0
        for i in range(1, n + 1):
            if i in visit:
                continue
            visit.add(i)

            component = get_connected_component(i)

            max_cnt = 0
            for src in component:
                length = get_longest_path(src)    
                if length == -1:
                    return -1
                max_cnt = max(max_cnt, length)
            
            res += max_cnt
        return res