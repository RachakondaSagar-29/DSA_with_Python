#---Queue follows First in first out (FIFO)
# we need to import deque (dobule ended queue - which adding and deletion can be happend from both sides) from collections.
from collections import deque
q=deque()
print(q)

#---adding elements in the queue (right side)----O(1)

q.append(5)
q.append(3)
q.append(8)
q.append(2)

print(q)

#----deque (pop left)---remove the element from the left --O(1)

q.popleft()
print(q)

##---peek from the left side--o(1)
print(q[0])

#---peek from the right side--o(1)
print(q[-1])