s=set()
print(s)

#---adding into set---O(1)
s.add(2)
s.add(5)
s.add(7)

print(s)

#---seraching if an iteam in the set -----O(1)

if 5 in s:
    print(True)

#----remove an element from the set---O(1)

s.remove(5)
print(s)

#----searching an alphabet in a string
# basically it is called as set constrcution --O(s)----s is the length of the string

string="aababababajakjhjhjjulklkloooiioioedrdrdrd"
sett=set(string)
print(sett)