# bubble sort
# time complexity : O(n^2)
# space complexit:  O(1)

A=[-5,4,8,10,-4,7,3,6,9,0]

def bubble_sort(arr):
    n=len(arr)
    flag=True
    while flag:
        flag=False
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                flag=True
                arr[i-1],arr[i]=arr[i],arr[i-1]
    return arr
print(bubble_sort(A))


#------------- insertion sort 

# time complexity:O(n^2)
# space complexity :O(1) -- adjusting elements

def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
            else:
                break
        return arr
print(insertion_sort(A))

# selection sort
# time:o(n^2)
# space : O(1)

def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index=i
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
print(selection_sort(A))



#---merge sort
# time : O(n log n)
# space : O(log n)

def merge_sort(arr):
    n=len(arr)

    if n==1:
        return arr

    m = len(arr)//2
    L=arr[:m]
    R=arr[m:]

    L=merge_sort(L)
    R=merge_sort(R)

    l,r=0,0
    L_len =len(L)
    R_len =len(R)

    sorted_arr=[0]*n
    i=0

    while l < L_len and r < R_len:
        if L[l]<R[r]:
            sorted_arr[i]=L[l]
            l += 1
        else:
            sorted_arr[i]=R[r]
            r += 1

        i +=1

    while l < L_len :
        sorted_arr[i]=L[l]
        l+=1
        r+=1

    while r<R_len:
        sorted_arr[i]=R[r]
        r+=1
        i+=1

    return sorted_arr

print(merge_sort(A))

# quick sort
# time : O(n log n) if you find good pivot
# if not O(n^2) 
# space: O(n)

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    
    P=arr[-1]
    L=[x for x in arr[:-1] if x <= P]
    R=[x for x in arr[:-1] if x > P ]

    L=quick_sort(L)
    R=quick_sort(R)

    return L + [P] + R
print(quick_sort(A))


#counting sort 
# time : O(n+k) where k is the range of data
# space: O(K)
# this is only on positive numbers
B=[3,6,8,3,5,2,3,7,2,6,7,4,9,5,7]
def counting_sort(arr):
    n=len(arr)
    maxx=max(arr)
    counts=[0]*(maxx+1)

    for x in arr:
        counts[x] += 1
    i=0
    for c in range(maxx+1):
        while counts[c] > 0:
            arr[i]=c 
            i +=1
            counts[c] -=1
    return arr

print(counting_sort(B))


# usually do in practise
# time complexity is O(n log n) from using Tim sort 

# Inplace (constant space)

B.sort()
print(B)

# get sorted arry-O(n) space
 
sorted_B=sorted(B)
print(B)

# # ## sorted array of tuples

I=[(-5,6),(2,3),(9,1),(5,7),(-7,4),(-4,6)]  # instervals

sorted_I=sorted(I,key= lambda t:t[1]) # t[0]--first palce of tuple t[1]--second place of tuple ,, if you put -t[0] it will sort reverse

print(sorted_I)
