"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take
course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1. Return the ordering of
courses you should take to finish all courses. If there are many valid answers, return any of them. If it is
impossible to finish all courses, return an empty array.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]] Output: [0,1] Explanation: There are a total of 2 courses to take. To
take course 1 you should have finished course 0. So the correct course order is [0,1].

Link: https://leetcode.com/problems/course-schedule-ii/
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = collections.defaultdict(list)
        res = []
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited, completed = set(), set()

        def dfs(crs):
            if crs in visited:
                return False
            if crs in completed:
                return True

            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)
            completed.add(crs)
            res.append(crs)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return res