# def add(num1, num2):  #deaful arguments
#     return num1 + num2

# result = add(1,258)
# print(result)

# def add(num1, *num2): #variable lenght argument ==== it returns a tuple

#     sum = num1
#     for n in num2:
#         sum += n
    
#     return sum


# result = add(8,6,3,5)

# print(result)

def person(name, **kwlargs):  #Keyword Lenght Arguments ==== it returs a Dictinary
  return name, kwlargs

result = person(name = "Papu", age = 30, loc = "Tlaquepunk", tech = "Python")

print(result)
