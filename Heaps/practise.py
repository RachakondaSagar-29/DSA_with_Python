# Build Min Heap (Heapify)
# Time: O(n), Space: O(1)

A = [5,0,4,-1,6,3,10,7,-4]

import heapq
heapq.heapify(A)  # heapq is a library, heapify is a function in it.

print(A)

# heap push -- inserting an element in to the heap
# time complexit will take O(n)

heapq.heappush(A,8)
print(A)

# heap pop--extracxting the min value form the heap
# time complexity : O(log n)-- becaues need to arrange the tree after poping the last element

minn=heapq.heappop(A)
print(A,minn)

# heap push pop-- basically it will push an element simuntaneously pops the root element

heapq.heappushpop(A,99)
print(A)

# heap sort 
# time complexity : (n log n) space : O(n)
# O(1) space is possible by swapping but it is complex

def heap_sort(arr):
    heapq.heapify(arr)
    n=len(arr)
    new_list=[0]*n
    for i in range(n):
        minn=heapq.heappop(arr)
        new_list[i]=minn

    return new_list
print(heap_sort(A))


# there is no function MAX Heap, so we will approch them in different way, making them into smallest first
 
B=[3,8,-2,6,9,1,23,5,9,4]

n=len(B)
for i in range(n):
    B[i]=-B[i]

heapq.heapify(B)
print(B)

# now we have to make them back as a largest element
largest=-heapq.heappop(B)
print(largest)

# if we wanted to give the new element into the max heap, you have to give negative number of what you wanna acutally give

heapq.heappush(B,-7)

print(B)



# building the heap from scratch...

C=[-9,5,6,2,3,8,10]
 
heap=[]

for x in C:
    heapq.heappush(heap,x)
    print(heap,len(heap)) # to check how many elemets are there in heap


# putting tuples of iteams on the heap

D=[5,5,6,7,8,5,6,8,7,7,8,8,6,6]

from collections import Counter

Counter=Counter(D)

print(Counter)

heap=[]
for k,v in Counter.items():
    heapq.heappush(heap,(v,k))

print(heap)


