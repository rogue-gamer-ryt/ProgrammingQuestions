"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value,
and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be
accepted.

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Link: https://leetcode.com/problems/find-median-from-data-stream/
"""
class MedianFinder:

    def __init__(self):
        self.minHeap, self.maxHeap = [], []

        # Array: [1, 2, 3, 4, 4, 5, 6, 7, 8]
        # MinHeap: [4, 5, 6, 7, 8]
        # MaxHeap: [4, 3, 2, 1]

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -1 * num)

        if len(self.minHeap) > len(self.maxHeap) + 1:
            num = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * num)
        elif len(self.maxHeap) > len(self.minHeap) + 1:
            num = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, num)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + (-1) * self.maxHeap[0]) / 2

        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return (-1) * self.maxHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()