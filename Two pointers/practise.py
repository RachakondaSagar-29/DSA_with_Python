# Arr=[-4,-1,0,3,10]
Arr=[-7,-3,2,3,11]
result=[]
for i in Arr:
    result.append(i**2)
print(sorted(result))


# using two pointers 

left=0
right=len(Arr)-1
results=[]
while left <= right:
    if abs(Arr[left]) > abs(Arr[right]):
        results.append(Arr[left]**2)
        left +=1
    else:
        results.append(Arr[right]**2)
        right -=1
results.reverse()
print(results)


