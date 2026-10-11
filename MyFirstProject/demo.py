
import math as m
#from math import sqrt

def add(a, b):
    """Adds two values"""
    c = a + b
    return c

result = add(5,6)
#print("result is",result)

#print(int(m.sqrt(25)))



#Swap Variables Values

a = input()
b = input()

print("a:",a, "b:", b)

a = a^b
b = a^b
a = a^b

print("a:",a, "b:", b)