# a = input("Enter a number: ")
# b = input("Enter another number: ")

# # print("Before swapping:", a, b)

# a, b = b, a

# print("After swapping:", a, b)

# ------------------------ but but but ----------------------------:
a = input("Enter a number: ") #-> str
b = input("Enter another number: ") #-> str

print(f"{a=}, {b=}")

c = a + b

print(f"sum of two numbers, {c=}") # a=3, b=5, c=35 # as input function returns string, so it will do string concatenation

# ------------------------

a = int(input("Enter a number: ")) #-> int
b = int(input("Enter another number: ")) #-> int

print(f"{a=}, {b=}")

c = a + b

print(f"sum of two numbers, {c=}")