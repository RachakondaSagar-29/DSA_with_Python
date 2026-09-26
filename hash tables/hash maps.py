#---hash map are generally dictionaries

d={'sagar':1,'racha':2,'konda':3}

print(d)

# adding a value ---
d['hello']=10

print(d)

#searching the key in the dictionary

if 'sagar' in d:
    print(True)

# checking the value of the given key

print(d['sagar'])

# getting iteams form the dictionary

for key,val in d.items():
    print(f"key :{key} and value : {val}")

# deafault dict

from collections import defaultdict
default=defaultdict(int)
print(default[2])
print(default)


#----counter

string="flwebfuiwgbuiwrbgwrbggqliughqeurgilurelgfur"

from collections import Counter
counter=Counter(string)
print(counter)
