"""
Write a program for the knapsack problem that selects a subset of items that has maximum value
and satisfies the weight constraint. All items have integer weights and values. Return the value of
the subset
"""

Items = collections.namedtuple("Items", ("weight", "value"))

# Time - O(nc) | Space - O(nc)
def optimum_subject_to_capacity(items, capacity):
    # Returns the optimum value when we choose from items[:k + 1] and have a 
    # capacity of available_capactiy
    def optimum_subject_to_item_and_capacity(k, available_capacity):
        if k < 0:
            return 0
        if V[k][available_capacity] == -1:
            without_curr_item = optimum_subject_to_item_and_capacity(k - 1, available_capacity)
            if available_capacity < items[k].weight:
                with_curr_item = 0    
            else:
                with_curr_item = items[k].value + 
                    optimum_subject_to_item_and_capacity(k - 1, available_capacity - items[k].weight)
            V[k][available_capacity] = max(without_curr_item, with_curr_item)
        return V[k][available_capacity]


    V = [[-1] * (capacity + 1) for _ in items]
    return optimum_subject_to_item_and_capacity(len(items) - 1, capacity)