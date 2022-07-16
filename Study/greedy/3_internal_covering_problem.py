"""
You are given a set of closed intervals. Design an efficient algorithm for finding a minimum sized
set of numbers that covers all the intervals.

Task times = [0,3] [2,6] [3,4] [6,9]
Best case - 3,6
"""
Interval = collections.namedtuple('Interval', ('left', 'right'))

def find_minimum_visits(intervals):
    intervals.sort(key=operator.attrgetter('right'))
    last_visit_time, num_visits = float('-inf'), 0
    for interval in intervals:
        if interval.left > last_visit_time:
            
            last_visit_time = interval.right
            num_visits += 1
    return num_visits
