# naive O(n) searching
A=[-3,-2,4,5,8,9]
if 4 in A:
    print(True)

# TC :O(log n)
# SC : O(1)

def binary_serach(A,target):
    N=len(A)
    L=0
    R=N-1
    while L<=R:
        M = L+((R-L)//2)

        if A[M]==target:
            return True
        elif target < A[M]:
            R=M-1
        else:
            L=M+1
    return False
print(binary_serach(A,6))