# Decorators: A function that takes another function as an argument, which is then called inside the outer function

def divide(a,b):
    return a / b

res = divide(10,2)
print(res)

# --------------- using decorators

def greater_decorator(func):
   
   def warp(a, b):
       if a < b:
           a, b = b, a
       return func(a, b)
   
   return warp

@greater_decorator
def divide(a, b):
    return a / b

res = divide(3, 21);
print(res)

# BTS of decorators:
# divide = divide_decorator(divide)
# res = divide(3, 21);
# print(res)

#------------------------------------------------------
# what if there are multiple parameters?
# def greater_decorator(func):
   
#    def warp(a, b):
#        if a < b:
#            a, b = b, a
#        return func(a, b)
   
#    return warp

# -> will not work

def greater_decorator(func):
    def warp(*args):
        # Sort numbers from smallest to largest
        sorted_args = sorted(args)
        # Take only the largest 3 items (the last 3 elements)
        largest_three = sorted_args[-3:]
        # Pass the unpacked tuple to the function
        return func(*largest_three)
    return warp

# 1. Renamed function to avoid naming conflict with built-in sum()
@greater_decorator
def sum_largest(*args):
    print(args)
    return sum(args)

# 78, 56, and 21 are the largest 3 numbers. 
# Total should be: 78 + 56 + 21 = 155
res = sum_largest(3, 21, 2, 56, 78)
print(res)  # Output: 155
