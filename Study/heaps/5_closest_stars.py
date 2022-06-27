"""
Consider a coordinate system for the Milky Way, in which Earth is at (0,0,0). Model stars as points,
and assume distances are in light years. The Milky Way consists of approximately 1012 stars, and
their coordinates are stored in a file.
How would you compute the k stars which are closest to Earth?
"""

# Since we need to find the closest to earth(distances should be smallest)
# We would use a max heap to pop the max values at k + 1

# Time - O(nlogk) | Space - O(k)
class Star:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    @property
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __lt__(self, rhs):
        return self.distance < rhs.distance

def find_closest_k_stars(stars, k):
    max_heap = []
    for star in stars:
        # Add each star to max heap
        # Since heapq only has min-heap, we can create a max heap by making the tuple
        # (negative of distance, star) to sort in reverse order
        heapq.heappush(max_heap, (-star.distance, star))
        if len(max_heap) == k + 1:
            heapq.heappop(max_heap)
    
    # Sorted from furthest to closest
    return [s[1] for s in heapq.nlargest(k, max_heap)]
