# set : collection of unordered unique items
# set is mutable
# set is unordered
# set is iterable

s = {33, 22, 44, 88, 22, 55, 55}
# print(s) # stored based on hash value
# print(type(s))

# print(22 in s) # True
# print(22 not in s) # False

#empty set:
set1 = {};
print(type(set1)) # <class 'dict'>

set2 = set();
print(type(set2)) # <class 'set'>

set3 = set("sandip");
# print(set3) # {'s', 'n', 'd', 'i', 'p'}

# set methods:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7, 8} # removes duplicates
print(set1.intersection(set2)) # {4, 5} # common elements in both
print(set1.difference(set2)) # {1, 2, 3}
print(set1.issubset(set2)) # False
print(set1.issuperset(set2)) # False

print(set1 - set2) # {1, 2, 3} # elements in set1 but not in set2
print(set2 - set1) # {6, 7, 8} # elements in set2 but not in set1
print(set1 | set2) # {1, 2, 3, 4, 5, 6, 7, 8} # union
print(set1 & set2) # {4, 5} # intersection
print(set1 ^ set2) # {1, 2, 3, 6, 7, 8} # symmetric difference