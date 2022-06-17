def random_sampling(k, A):
  for i in range(k):
    # Generate a random index in [i, len(A) - 1]
    r = random.randint(i, len(A) - 1)
    A[r], A[i] = A[i], A[r]

# If k > n/2 then generate subset of n - k elements and then remove this set from the array


# This problem is motivated by the design of a packet sniffer that provides a uniform sample of
# packets for a network session.
# Design a program that takes as input a size k, and reads packets, continuously maintaining a
# uniform random subset of size k of the read packets.

def online_random_sample(it, k):
  # First k elemenets
  sampling_results = list(itertools.islics(it, k))

  # Have read the first k elements
  num_seen_so_far = k
  for x in it:
    num_seen_so_far += 1
    # Genreate a random number in [0m num_seen_so_far - 1] and if the number is in [0, k-1],
    # we replace that element from the sample with x
    idx_to_replace = random.randrange(num_seen_so_far)
    if idx_to_replace < k:
      samplint_results[idx_to_replace] = x
  return sampling_results
