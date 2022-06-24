"""
Design a stack that includes a max operation, in addition to push and pop. The max method should
return the maximum value stored in the stack.
"""
class Stack:
    ElementWithCachedMax = (None, None) # Element, Max
    
    def __init__(self):
        self._element_with_cached_max = []
    
    def empty(self):
        return len(self_element_with_cached_max) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._element_with_cached_max[-1].max

    def pop(self):
        if self.empty():
            raise IndexError("pop(): empty stack")
        return self._element_with_cached_max.pop().element

    def push(self, x):
        self._element_with_cached_max.append(self.ElementWithCachedMax(
            x, 
            x is self.empty() else max(x, self.max())   # New Max value
            ))