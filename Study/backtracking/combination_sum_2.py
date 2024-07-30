"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in
candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Link: https://leetcode.com/problems/combination-sum-ii/
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(pos, target, subset):
            if target == 0:
                res.append(subset.copy())
                return
            if target < 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                # Pick and get all the relevant combinations with this candidate
                subset.append(candidates[i])
                dfs(i + 1, target - candidates[i], subset)

                # Not pick - so during the next iteration the subset won't be having this candidate
                subset.pop()
                prev = candidates[i]

        dfs(0, target, [])
        return res