a = 5
b = 5

print(id(a)) # 140731952874536
print(id(b)) # 140731952874536
# for variables a and b, both have same memory address, a & b are just references (same box [5])

print(a is b) # True

b = 6
print(id(b)) # 140731952874568
print(a is b) # False # a and b have different memory address (different box [5] & [6])

#  but:
c = {1: "Hello"};
d = {1: "Hello"};

print(c is d) # False # although c and d looks same, they have different memory address 


n = 'sandip'
m = 'sandip'

print(id(n) == id(m)) # True, for small strings it can be True

n = "Hey there! how are you?"
m = "Hey there! how are you?"

print(id(n) == id(m)) # False # sometimes it can be True. depending on interpreter


#range:
r = range(10)
print(r) # range(0, 10)

set(r) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
set(range(2, 10, 2)) # {2, 4, 6, 8} # range(start, end, step)


tup = (2, 3)
print(list(tup)) # [2, 3] # convert tuple to list