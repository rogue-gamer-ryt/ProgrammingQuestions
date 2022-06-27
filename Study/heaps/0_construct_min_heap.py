"""
Based on a given array. Construct a mean heap data structure
"""

class MinHeap:
    def __init__(self, array):       
        self.heap = self.buildHeap(array)
    
    # Time Complexity - O(n) | Space - O(1)
    def buildHeap(self, array):
        first_parent_idx = (len(array) - 1) // 2
        for curr_idx in reversed(range(first_parent_idx + 1)):
            self.siftDown(curr_idx, len(array) - 1, array)
        return array
        
    # Time Complexity - O(log(n)) | Space - O(1)
    def siftDown(self, start_idx, end_idx, heap):
        curr_idx = start_idx
        child_1_idx = 2 * curr_idx + 1
        
        while child_1_idx <= end_idx:
            child_2_idx = 2 * curr_idx + 2 if curr_idx * 2 + 2 <= end_idx else -1 
            # Get the min child
            if child_2_idx != -1 and heap[child_2_idx] < heap[child_1_idx]:
                min_child_idx = child_2_idx
            else:
                min_child_idx = child_1_idx
            # perform swapping operations
            if heap[curr_idx] > heap[min_child_idx]:
                heap[curr_idx], heap[min_child_idx] = heap[min_child_idx], heap[curr_idx]
                curr_idx = min_child_idx
                child_1_idx = 2 * curr_idx + 1
            else:
                return

    # Time Complexity - O(log(n)) | Space - O(1)
    def siftUp(self, start_idx, end_idx, heap):
        curr_idx = start_idx
        parent_idx = (curr_idx - 1)// 2
        while curr_idx > 0 and heap[curr_idx] < heap[parent_idx]:
            # perform swapping operations
            heap[curr_idx], heap[parent_idx] = heap[parent_idx], heap[curr_idx]
            curr_idx = parent_idx
            parent_idx = (curr_idx - 1)// 2
    
    # Time Complexity - O(1) | Space - O(1)
    def peek(self):
        return self.heap[0]

    # Time Complexity - O(log(n)) | Space - O(1)
    def remove(self):
        # remove root and swap with last elment
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_value = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return min_value

    # Time Complexity - O(log(n)) | Space - O(1)
    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, 0, self.heap)
