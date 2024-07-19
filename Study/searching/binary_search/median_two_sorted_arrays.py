"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2
        l, r = 0, len(A) - 1

        while True:

            i = (l + r) // 2  # Partition from A
            j = half - i - 2  # Partition from B

            ALeft = A[i] if i >= 0 else float("-inf")
            ARight = A[i + 1] if (i + 1) < len(A) else float("inf")
            BLeft = B[j] if j >= 0 else float("-inf")
            BRight = B[j + 1] if (j + 1) < len(B) else float("inf")

            if ALeft <= BRight and BLeft <= ARight:
                # Parittion is correct
                if total % 2:
                    return min(ARight, BRight)

                return (max(ALeft, BLeft) + min(ARight, BRight)) / 2

            elif ALeft > BRight:
                r = i - 1
            else:
                l = i + 1
