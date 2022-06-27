"""
Suppose you were asked to write a program which takes a sequence of strings presented in "streaming"
fashion: you cannot back up to read an earlier value. Your program must compute the k longest
strings in the sequence. All that is required is the k longest strings-it is not required to order these
strings.
As we Process the input, we want to track the k longest strings seen so far. Out of these k strings,
the string to be evicted when a longer string is to be added is the shortest one.
"""
# We will use min heap as then removal of the min elment would only take log(n) and the remaining elements would be the maximum elements from the stream

import itertools
import heapq

# time - O(nlogk) - At the any time the length of min_heap is k
def top_k(stream, k):
    # Create a min heap - as an array
    min_heap = [(len(s), s) for s in itertools.islice(stream, k)]
    heapq.heapify(min_heap)

    for next_string in stream:
        # Push the next string in the min_heap and pop the shortest string
        # In heapq the 1st element of the tuple is considered as the key while comparision
        heapq.heappushpop(min_heap, (len(next_string), next_string))

    # The heap would at any point only have k items(since we are pushing and poping) so the nlargest and
    # nsmallest is just the order of items you want to return in
    return [p[1] for p in heapq.nlargest(k, min_heap)]

assert top_k(["ab", "ab3","abc", "abcd", "abbbbbb", "a", "ab", ""], 3) == ['abbbbbb', 'abcd', 'abc']