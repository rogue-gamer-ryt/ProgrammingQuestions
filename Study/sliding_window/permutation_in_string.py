"""
Given two strings s1 and s2, return true if s2 contains a
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Link: https://leetcode.com/problems/permutation-in-string/
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count, s2Count = [0] * 26, [0] * 26
        matches = 0

        for i in range(len(s1)):
            index1 = ord(s1[i]) - ord("a")
            index2 = ord(s2[i]) - ord("a")
            s1Count[index1] += 1
            s2Count[index2] += 1

        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1

            # Update Matches when you add an element to the window
            # If it is a match then increase the match count
            # If the letter was a match before then unmatch it
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] == s1Count[index] + 1:
                matches -= 1

            # Update Matches when you remove an element to the window
            # If it is a match then increase the match count
            # If the letter was a match before then unmatch it
            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s2Count[index] + 1 == s1Count[index]:
                matches -= 1
            elif s2Count[index] == s1Count[index]:
                matches += 1
            l += 1

        return matches == 26
