class singlenode:
    def __init__(self,node,next=None):
        self.node=node
        self.next=next

    def __str__(self):
        return str(self.node)
head=singlenode(1)
A=singlenode(2)
B=singlenode(3)
C=singlenode(6)

head.next=A
A.next=B
B.next=C

print(head)
print(A)
print(B)
print(C)

#-------traverse --O(n)----------------

def traverse(head):
    curr=head
    while curr:
        print(curr)
        curr=curr.next
traverse(head)

# #-------display--O(n)----

def display(head):
    curr=head
    elements=[]
    while curr:
        elements.append(str(curr.node))
        curr=curr.next
    print(' -> '.join(elements))
display(head)

#----- search for a value----O(n)---------

def search(head,val):
    curr=head
    while curr:
        if curr.node==val:
            return True
        curr=curr.next
    return False 
print(search(head,6))

#---inser at the begginnig --O(n)

def insert_at_beginning(head,val):
    new_node=singlenode(val)
    new_node.next=head
    head=new_node
    return head
head=insert_at_beginning(head,5)
print(head)
curr=head
elements=[]
while curr:
    elements.append(str(curr.node))
    curr=curr.next
print(" -> ".join(elements))

#----insert at the end-----O(n)

def insert_at_end(head,val):
    new_node=singlenode(val)
    if head is None:
        return new_node
    curr=head
    while curr.next:
        curr=curr.next
    curr.next=new_node
    return head
head=insert_at_end(head,10)
print(head)


        

    

