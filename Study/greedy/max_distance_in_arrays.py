"""
You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define
the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.



Example 1:

Input:
arrays = [[1,2,3],[4,5],[1,2,3]] Output: 4 Explanation: One way to reach the maximum distance 4 is to pick 1
in the first or third array and pick 5 in the second array.

Link: https://leetcode.com/problems/maximum-distance-in-arrays/
"""

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = float('-inf')
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        for i in range(1, len(arrays)):
            minVal, maxVal = arrays[i][0], arrays[i][-1]
            res = max(res, abs(minVal - biggest), abs(smallest- maxVal))
            smallest = min(smallest, minVal)
            biggest = max(biggest, maxVal)


        return res