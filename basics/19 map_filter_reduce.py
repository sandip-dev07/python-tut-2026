from functools import reduce

# ------------------------ Filter
nums = [4, 2, 5, 7, 9, 1 , 3, 6, 8, 0]

evens = []

for i in nums:
    if(i & 1 != 1):
        evens.append(i)

# evens.sort()
print(sorted(evens))
    
    
def func(x):
    return x & 1 == 1

odds = list(filter(func, nums))
print("odds",odds)

# using lambda:
odds = list(filter(lambda x : x & 1 == 1, nums))
print("odds",odds)


greater_val = list(filter(lambda x: x > 5, nums))
print("greater_val",greater_val)

# ------------------ Map
doubles = list(map(lambda x: x * 2, evens))
print("doubles",doubles)

# ------------------ Reduce
total = reduce(lambda x, y: x + y, odds)
print("total",total)

# ------------------ Chaining
# write a one liner python code to find the sum of cubes of odd numbers in a list
sum = reduce(lambda x, y: x + y, list(map(lambda x: x ** 3, [1, 2, 3])))
print("sum",sum)