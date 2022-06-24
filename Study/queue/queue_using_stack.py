"""
Queue insertion and deletion follows first-in, first-out semantics; stack insertion and deletion is
last-in, first-out.

How would you implement a queue given a library implementing stacks?
"""

# Have  two queues
# 1. For enqueue
# 2. For dequeue
# During insertion we push it to enqueue
# While dequeue we check if dequeue is empty
# If yes, we pop all elements from enqueue to dequeue and then get the topmost value
# If no, we get the top most value

# Time complexity: O(m) for m operations
class Queue:
    def __init__(self):
        self._enq, self._deq = [], []
    
    def enqueue(self, val):
        self._enq.append(val)
    
    def dequeue(self):
        if not self._deq:
            while self._enq:
                self._deq.append(self._enq.pop())
        if not self._deq:
            # If it is still empty
            raise IndexError('empty queue')
        return self._deq.pop()


