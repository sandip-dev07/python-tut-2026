# functions:

# print("test!")

def add(a: int, b: int) -> int:
    """ This function adds two numbers and returns the result. """ # docstring
    c = a + b
    return c

x = add(3, 4)
# print(x)

x = add(5, 8)
# print(x)


# ------------------ Arguments in function:

# with default value:
def add(a = 0, b = 0):
    return a + b

x = add(5, 6)
print(x)

# ------------------- *args and **kwargs:
# *args: tuple
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

x = add(1, 2, 3, 4, 5)
print(x)

# **kwargs (keyword arguments): dictionary
def add(**kwargs):
    sum = 0
    for i in kwargs.values():
        sum += i
    return sum

x = add(a = 1, b = 2, c = 3, d = 4, e = 5)
print(x)


# ------------------ difference between *args and **kwargs

# *args: takes variable number of arguments as a tuple
# **kwargs: takes variable number of arguments as a dictionary

# def add(*args, **kwargs):
#     sum = 0
#     for i in args:
#         sum += i
#     for i in kwargs.values():
#         sum += i
#     return sum