# Build heap from scratch - Time: O(n log n)

C = [-5, 4, 2, 1, 7, 0, 3]

heap = []

for x in C:
  heapq.heappush(heap, x)
  print(heap, len(heap)) # Check size of heap

# Putting tuples of items on the heap

D = [5, 4, 3, 5, 4, 3, 5, 5, 4]

from collections import Counter

counter = Counter(D)

print(counter)

heap = []

for k, v in counter.items():
  heapq.heappush(heap, (v, k))

print(heap)