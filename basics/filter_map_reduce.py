from functools import reduce

nums = [1,2,3,4,5,6,7,8,9]

# evens = []

# for i in nums:
#     if i % 2 == 0:
#        evens.append(i)


evens = list(filter(lambda n : n % 2 == 0, nums))
doubles = list(map(lambda n: n*2, evens))
sum = reduce(lambda a,b : a+b, doubles)

print("Evens: ", evens)
print("Doubles: ",doubles)
print("Sum: ", sum)