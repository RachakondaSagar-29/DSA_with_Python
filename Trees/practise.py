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

print(A)
