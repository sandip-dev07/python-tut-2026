# Lambda function: anonymous function without name

def func(x):
    return x * x

x = func(3)
print(x)

cube = lambda num : num * num * num
x = cube(3)
print(x)

add = lambda a, b : a + b
x = add(3, 4)
print(x)