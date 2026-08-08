# module: collection of functions, variables, classes, etc.

from math import sqrt, pow, ceil, fabs # Math is a module containing math functions

num = 25;
res = sqrt(num);

# print(res)

num = 25;
res = pow(num, 2);

# print(res)


x = -10.7
y = 3

# print(ceil(x))
# print(fabs(x)); # it removes any negative sign and always yields a positive decimal value
# print(pow(y, 2))

# --------------------------------------------

#swapping variables:

a = 5
b = 10

# Correct way
print(f"{a=}, {b=}")

# a, b = b, a # tuple packing & tuple unpacking

a = a + b # 5 + 10 = 15
b = a - b # 15 - 10 = 5
a = a - b # 15 - 5 = 10

print(f"{a=}, {b=}")

a = a ^ b
b = a ^ b
a = a ^ b

print(f"{a=}, {b=}")