# Array of Edges (Directed) [Start, End]
n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

# covert array of edges ---> adjacency matrix

m=[]

for i in range(n):
    m.append([0]*n)

for u,v in A:
    m[u][v]=1
# Uncomment the following line if the graph is undirected
  # M[v][u] = 1

print(m)


## convert array of edges -----> adjacency list

from collections import defaultdict

D=defaultdict(list)

for u,v in A:
    D[u].append(v)
# Uncomment the following line if the graph is undirected
  # D[v].append(u) = 1
print(D)


# DFS with Recursion - O(V + E) where V is the number of nodes and E is the number of edges

def depth_first_serach(node):
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            depth_first_serach(nei_node)


source=0
seen=set()
seen.add(source)
depth_first_serach(source)

# Iterative DFS with Stack - O(V + E)
print("-----BFS------")
source=0
seen=set()
seen.add(source)
stack=[source]

while stack:
    node=stack.pop()
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            stack.append(nei_node)

# BFS (Queue) - O(V + E)

source = 0

from collections import deque

seen = set()
seen.add(source)
q = deque()
q.append(source)

while q:
  node = q.popleft()
  print(node)
  for nei_node in D[node]:
    if nei_node not in seen:
      seen.add(nei_node)
      q.append(nei_node)

#-------creating graphs from scratch--------
class Node:
  def __init__(self, value):
    self.value = value
    self.neighbors = []

  def __str__(self):
    return f'Node({self.value})'

  def display(self):
    connections = [node.value for node in self.neighbors]
    return f'{self.value} is connected to: {connections}'

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

A.neighbors.append(B)
B.neighbors.append(A)

C.neighbors.append(D)
D.neighbors.append(C)

print(B.display())