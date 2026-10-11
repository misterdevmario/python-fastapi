


def square (num):

   return num ** 2

def cube (num):
   return num ** 3

def operation(num, op):
   return(op(num))

value = 3

result = operation(value, square)

print(result)
