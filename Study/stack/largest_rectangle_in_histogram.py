"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Link: https://leetcode.com/problems/largest-rectangle-in-histogram/
"""
from typing import List


# Time Complexity: O(n)
# Go over each height and then check if it was higher than the item at the top of the stack. If not, then pop the item
# out as you can't extend the area of the top most item in stack now. Calculate its Area and then check if it's maximum
# or not.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # pair: (index, height)
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)

        return maxArea