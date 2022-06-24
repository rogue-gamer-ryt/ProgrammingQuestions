"""
A queue can be implemented using an array and two additional fields, the beginning and the end
indices. This structure is sometimes referred to as a circular queue. Both enqueue and dequeue
have O(1) time complexity. If the array is fixed, there is a maximum number of entries that can be
stored. If the array is dlmamically resized, the total time for rn combined enqueue and dequeue
operations is O(m).

Implement a queue API using an array for storing elements. Your API should include a constructor
functioru which takes as argument the initial capacity of the queue, enqueue and dequeue functions,
and a function which retums the number of elements stored. Implement dynamic resizing to
support storing an arbitrarily large number of elements.
"""

# Have head to keep track of the current head so while dequeue you shift the head and pop it

# Time complexity - O(1) [dequeue and enqueue]
class Queue:
    SCALE_FACTOR = 2

    def __init__(self, capacity):
        self._entries = [None] * capacity
        self._head = self._tail = self._num_queue_elements = 0
    
    def enqueue(self, x):
        if self._num_queue_elements == len(self._entries): # Needs to resize
            # Makes the queue elements appear consecutively
            self._entries = (
                self._entries[_head:] + self._entries[:self._head]
            )
            # Reset head and tail
            self._head, self._tail = 0, self._num_queue_elements
            # Add more elements so the array grows based on SCALE_FACTOR
            self._entries += [None] * (
                len(self._entries) * Queue.SCALE_FACTOR - len(self._entries)
                )
        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        self._num_queue_elements += 1

    def dequeue(self):
        if not self._num_queue_elements:
            # No elements in the queue
            return None
        self._num_queue_elements -= 1
        ret = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        return ret

    def size(self):
        return self._num_queue_elements

