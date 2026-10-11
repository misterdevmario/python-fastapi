
import sys


# Way to calculate a factorial using recursion

def fact(num):
    if num == 1: return 1

    return num * fact(num - 1) 
result = fact(5)
print(result)


