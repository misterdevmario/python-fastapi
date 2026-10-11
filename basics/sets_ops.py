# print(set(range(5,100,10)))
# print(list(range(5,110,10)))

# Arithmetic Operators

l1 = [1,2, 2, 2, 2]

# in divisions // is a cocient operator and % the mod oprator which indicates the number of units needed left after the division was perprmed, for example 5/2 = 2.5 but the integer in this case is the reminder = 1

s1 = {1,2,3,4,5}
s2 = {6,7,8,1,5}

set1 = set('papu')
set2 = set('papurobot')



#print(set2 | set1)
# print(s1 - s2)
# print(s2 - s1) # Returns values that only exits in set l2 removing also those in common in s2
# print(s2 & s1) # Returns values in common
# print(s2 ^ s1) # Returns values not in common

ska = {1:"ska"}

keys = {"1","2","3"}
values = [1,2,3]

dict1 = dict(zip(keys, values))

poped = dict1.pop("1")

print(poped)