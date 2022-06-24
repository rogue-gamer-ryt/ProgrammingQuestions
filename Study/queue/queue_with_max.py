"""
Implement a queue with enqueue, dequeue, and max operations. The max operation refurns the
maximum element currently stored in the queue.
"""


# Time complexity - 
#   dequeue - O(1)
#   enqueue - O(1)
class QueueWithMax:
    def __init__(self):
        self._entries = collections.deque()
        self._candidates_for_max = collections.deque()
    
    def enqueue(self, val):
        self._entries.append(val)
        while self._candidates_for_max and self._candidates_for_max[-1] < x:
            self._candidates_for_max.pop()
        self._candidates_for_max.append(val)
    
    def dequeue(self):
        if self._entries:
            result = self._entries.popleft()
            if result == self._candidates_for_max[0]:
                self._candidates_for_max.popleft()
            return result
        raise IndexError('empty queue')
    
    def max(self):
        if self._candidates_for_max:
            return sefl._candidates_for_max[0]
        raise IndexError('empty queue')
        
        