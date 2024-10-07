"""
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],
[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings
without any conflicts.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2

Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

Link: https://neetcode.io/problems/meeting-schedule-ii | https://leetcode.com/problems/meeting-rooms-ii/
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for i in intervals:
            start, end = i.start, i.end
            time.append((start, 1))
            time.append((end, -1))
        # Sorting it based on both values makes
        # sure when a meeting is starting at 10 and a meeting is ending at 10
        # The tuple with end time comes before the tuple with start time.
        # Since we are also sorting it based on -1 (end) and 1 (start)
        time.sort(key=lambda x: (x[0], x[1]))

        count = 0
        max_count = 0
        for t in time:
            count += t[1]
            max_count = max(max_count, count)
        return max_count