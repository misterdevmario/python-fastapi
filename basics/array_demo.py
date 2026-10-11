from array import *

arr1 = array("i",[33,44,55,85])

#arr2 = array(arr1.typecode,arr1.tolist())
arr2 = array(arr1.typecode,(n for n in arr1))

arr1.append(7)

print(type(arr1))
print(type(arr2))
print(arr1)
print(arr2)