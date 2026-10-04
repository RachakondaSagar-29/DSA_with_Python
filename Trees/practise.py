class Treenode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    def __str__(self):
        return str(self.val)
A=Treenode(1)
B=Treenode(2)
C=Treenode(3)
D=Treenode(4)
E=Treenode(5)
F=Treenode(6)

A.left=B
A.right=C
B.left=D
B.right=E
C.left=F

# print(A)
# TREE would be like
#    1
#   2  3
#  4 5 6

print("--------------pre order traversal-----------------")
def pre_order(node):
    if not node:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)

pre_order(A)

print("--------------In order traversal-----------------")

def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node)
    in_order(node.right)

in_order(A)

print("-------------post order traversal---------------")
def post_order(node):
    if not node:
        return
    post_order(node.left)
    post_order(node.right)
    print(node)

post_order(A)


print("----------pre order traversal without using recursive function------")

def pre_order_iteration(node):
    stk=[node]
    while stk:
        node=stk.pop()
        print(node)
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)

pre_order_iteration(A)

print("bredth first search using with Queue")


from collections import deque

def level_order(node):
    q=deque()
    q.append(node)
    while q:
        node=q.popleft()
        print(node)
        if node.left:q.append(node.left)
        if node.right:q.append(node.right)

level_order(A)

print("searching for a element in tree using DFS")

def serach_val(node,target):
    if not node:
        return False
    if node.val == target:
        return True
    return serach_val(node.left, target) or serach_val(node.right, target)
print(serach_val(A,5))


# Binary Search Trees (BSTs)

#       5
#    1    8
#  -1 3  7 9

A2 = Treenode(5)
B2 = Treenode(1)
C2 = Treenode(8)
D2 = Treenode(-1)
E2 = Treenode(3)
F2 = Treenode(7)
G2 = Treenode(9)

A2.left, A2.right = B2, C2
B2.left, B2.right = D2, E2
C2.left, C2.right = F2, G2

print("searching an element in BST-------it takes TC--log n and SC--log n")

def search_bst(node,target):
    if not node:
        return False
    if node.val == target:
        return True
    if target < node.val: return search_bst(node.left,target)
    else:return search_bst(node.right,target)

print(search_bst(A2,-1))