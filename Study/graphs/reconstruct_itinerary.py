"""
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival
airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are
multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single
string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example 1:

Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Link: https://leetcode.com/problems/reconstruct-itinerary/
"""


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adj = collections.defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)

        res = []

        def dfs(src):
            dests = adj[src]
            while dests:
                next_destination = dests.pop()
                dfs(next_destination)
            res.append(src)
            return False

        dfs("JFK")
        return res[::-1]