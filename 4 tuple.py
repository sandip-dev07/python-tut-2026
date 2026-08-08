# tuple: immutable

tup = (1, 2, 3, 4, 5)
print(tup)
print(type(tup))

tup = (1, 2, 3, 4, 5)
print(tup[1]) # 2

print(max(tup))

# tuple methods
tup = (1, 2, 3, 4, 5, 3)
# print(tup.count(3)) # 1
# print(tup.index(3)) # 2


tupA = (2, "sandip", 4.5, True)
num, name, marks, status = tupA # tuple unpacking
# print(num, name, marks, status)

tupB = (2, "sandip", 4.5, [1, 2, 3])
tupB[3].append(4)
print(tupB)