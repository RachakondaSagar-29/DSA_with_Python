class doublelinkedlist:
    def __init__(self,node,next=None,pre=None):
        self.node=node
        self.next=next
        self.pre=pre 

    def __str__(self):
        return str(self.node)
head=tail=doublelinkedlist(3)

A=doublelinkedlist(4)
B=doublelinkedlist(10)
C=doublelinkedlist(35)


head.next=A
A.pre=head
A.next=B
B.pre=A
B.next=C
C.pre=B
tail=C


#-----display the elements ---O(n)
def display(head):
    curr=head
    elements=[]
    while curr:
        elements.append(str(curr.node))
        curr=curr.next
    print(" <-> ".join(elements))
    return head
display(head)


#--------insert at beginning --------O(1)
def insert_at_beginning(head,tail,node):
    new_node=doublelinkedlist(node,next=head)
    head.pre = new_node
    return new_node,tail
head,tail=insert_at_beginning(head,tail,5)

#--checking---
curr=tail
elements=[]
while curr:
    elements.append(str(curr.node))
    curr=curr.next
print(" <-> ".join(elements))

print(head,tail)

#-------inseart at end -----O(n)

def insert_at_end(tail,node):
    new_node=doublelinkedlist(node,pre=tail)
    tail.next=new_node
    return new_node
tail=insert_at_end(tail,9)
#---checking---
curr=head
elements=[]
while curr:
    elements.append(str(curr.node))
    curr=curr.next
print(" <-> ".join(elements))


#-----insert in middle------O(n)
def insert_at_given(head,node):
    curr=head
    while curr.node!=4:
        curr=curr.next
    new_node=doublelinkedlist(node)
    new_node.next=curr.next
    new_node.pre=curr
    curr.next.pre=new_node
    curr.next=new_node
    return head
head=insert_at_given(head,5)
print(head)
#--checking
curr=head
elements=[]
while curr:
    elements.append(str(curr.node))
    curr=curr.next
print(" <-> ".join(elements))