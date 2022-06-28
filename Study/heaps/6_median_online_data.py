"""
You want to compute the running median of a sequence of numbers. The sequence is presented to
you in a streaming fashion-you carmot back up to read an earlier value, and you need to output
the median after reading in each new element. For example, if the input is 1,0,3,5,2,0,1 the output
is 1,0.5,1,2,2,1.5,1

Design an algorithm for computing the running median of a sequence.
"""

# Median divides the array into two parts
# To calculate a median you need to have a sorted array
# If odd no. of elements then median = (n + 1) / 2th element
# If even no of elements then mdedian = (n/2th element + (n+2)/2th element)/2

# use max and min heap to store the larger half and smaller half
# max heap for smaller half
# min heap for larger half

def online_median(sequence):
    # min_heap stores the larger half seen so far
    min_heap = []
    # max_heap stores the smaller half seen so far
    # values in max_heap are negative
    max_heap = []
    result = []

    for x in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
        # min_heap and max_heap should have the same length if an even number of elements is read;
        # otherwise min_heap would have one more
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        result.append(0.5 * (min_heap[0] + -max_heap[0]) if len(min_heap) == len(max_heap) else min_heap[0])
        
        return result

# https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] + (-self.small[0])) / 2.0
        else:
            return float(self.large[0])

