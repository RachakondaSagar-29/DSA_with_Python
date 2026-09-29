#--- fibnacci series 
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(0,10):
    print(fib(i))

#----reversing a linked list using recursion function.
class singlelist:
    def __init__(self,node,next=None):
        self.node=node
        self.next=next

    def __str__(self):
        return str(self.node)

head=singlelist(1)
A=singlelist(2)
B=singlelist(3)
C=singlelist(4)

head.next=A
A.next=B
B.next=C

def reverse(node):
    if not node:    # ( node!=None )
        return
    reverse(node.next)
    print(node)
reverse(head)