# HOF: Higher Order Function, a function that takes a function as an argument

def square(x):
    return x * x

def cube(x):
    return x * x * x

def operate(val, func):
    return func(val)

print(operate(5, square))
print(operate(5, cube))