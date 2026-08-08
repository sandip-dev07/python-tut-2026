from array import *

lenght = int(input("Enter the length of the array: "))

arr = array('i', [])

for i in range(lenght):
    x = int(input("Enter the value: "))
    arr.append(x)

print(arr)