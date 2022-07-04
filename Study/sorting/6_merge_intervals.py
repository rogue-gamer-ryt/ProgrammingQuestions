"""
Write a program which takes as input an array of disjoint closed intervals with integer endpoints,
sorted by increasing order of left endpoint, and an interval to be added, and returns the union of
the intervals in the array and the added interval. Your result should be expressed as a union of
disjoint intervals sorted by left endpoint.
"""
Interval = collections.namedtuple('Interval', ('left', 'right'))

# Time - O(n)
def add_interval(disjoint_intervals, new_interval):
    i, result = 0, []

    # processes intervals in disjoint_intervals which come before new_interval
    while (
        i < len(disjoint_intervals)
        and new_interval.left > disjoint_intervals[i].right
        ):
        result.append(disjoint_intervals[i])
        i += 1
    
    # Process intervals in disjoint_intervals which overlap with new interval
    while (i < len(disjoint_intervals)
        and new_interval.right >= disjoint_intervals[i].left):
        # union would be [min(left1, left2), max(right1, right2)]
        new_interval = Interval(
            min(new_interval.left, disjoint_intervals[i].left),
            min(new_interval.right, disjoint_intervals[i].right)
        )
        i += 1

    # Append the remaining intervals
    return result + [new_interval] + disjoint_intervals[i:]





