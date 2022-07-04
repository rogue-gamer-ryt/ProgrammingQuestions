"""
In this problem we consider sets of intervals with integer endpoints; the intervals may be open
or closed at either end

Design an algorithm that takes as input a set of intervals, and outputs their union expressed as a
set of disjoint intervals.
"""

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.left.val != other.left.val:
            return self.left.val < other.left.val
        # Left endpoints are equal, so now see if one is closed and the other opn
        # - closed intervals should appear first
        return self.left.is_closed and not other.left.is_closed

    def union_of_intervals(intervals):
        if not intervals:
            return []
        # Sort the intervals according to left endpoints of intervals
        intervals.sort()
        result = [intervals[0]]

        for i in intervals:
            if intervals and (
                i.left.val < result[-1].right.val # Check if there is overlap
                or (
                    i.left.val == result[-1].right.val   # Check if both are equal then are the closed or open
                    and (i.left.is_closed or result[-1].right.is_closed)
                )
            ):
                if i.right.val > result[-1].right.val or (
                    i.right.val == result[-1].right.val and i.right.is_closed
                ):
                    result[-1].right = i.right
            else:
                result.append(i)
        return result
