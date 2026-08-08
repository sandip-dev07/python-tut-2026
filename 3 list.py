# list: (Array) collection of items
# list is mutable
# list is indexed
# list is ordered
# list is iterable

nums = [1, 2, 3, 4, 5]
# print(nums)
print(type(nums))

# print(nums[1:len(nums)-1]) # [2, 3, 4]

nums[1] = 10 # mutable
# print(nums)


names = ["Raju", "Reddy", "Sandip"]

mix = [nums, names] # nested: list of list: [[1, 10, 3, 4, 5], ['Raju', 'Reddy', 'Sandip']]
# print(mix[0])

mix = nums + names # list concatenation
print(mix)


# list methods:
nums = [4, 5, 6, 7, 8, 9, 10]
nums.append(6) # add at end
nums.insert(0, 55) # insert at index 0 : [55, 4, 5, 6, 7, 8, 9, 10, 6]
nums.remove(6) # remove first occurrence of 6
# nums.pop() # remove last element (default: -1 index)
nums.count(3) # count of 3: 1
# nums.clear()

nums.sort(reverse=True)
# nums.reverse()

del nums[4:] # delete from index 4 to end

nums.extend([11, 12, 13]) # add at end
nums[2:4] = [55, 66, 88]

print(nums)


# ----------------------------------------------------------------------
# tuple: (Tuple) collection of items
# tuple is immutable
# tuple is indexed
# tuple is ordered
# tuple is iterable
nums = 22, 33, 44, 55, 66
# print(nums)
# print(type(nums))


