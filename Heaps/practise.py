# Build Min Heap (Heapify)
# Time: O(n), Space: O(1)

A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

import heapq
heapq.heapify(A)

A

# Heap Push (Insert element)
# Time: O(log n)

heapq.heappush(A, 4)

A 
# Heap Pop (Extract min)
# Time: O(log n)

minn = heapq.heappop(A)

A, minn

# Heap Sort
# Time: O(n log n), Space: O(n)
# NOTE: O(1) Space is possible via swapping, but this is complex

def heapsort(arr):
  heapq.heapify(arr)
  n = len(arr)
  new_list = [0] * n

  for i in range(n):
    minn = heapq.heappop(arr)
    new_list[i] = minn

  return new_list

heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])