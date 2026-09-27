stk=[]
print(stk)

#-----last is first out policy (LIFO)

#-- adding an element into stack---o(1)
stk.append(5)
stk.append(8)
stk.append(2)
stk.append(9)

print(stk)

#-----pop() ---O(1)
x=stk.pop()
print(x)
print(stk)

#----- ask what is on the top of the stack

print(stk[-1])
