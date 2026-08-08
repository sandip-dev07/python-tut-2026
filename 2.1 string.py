# 1: concatenation
print('sandip' ' ' 'laptop') # string literal

# 2:
name = 'Raju'
# print(name 'Reddy') # now it will throw error, as variable name & string literal cannot be concatenated
print(name + 'Reddy') # works fine, as variable name & string literal can be concatenated via + operator

# 3:
text  = "Hello World"
print(text[0]) # H
# print(text[12]) # out of range
print(text[-1]) # d

# 4: slicing
print(text[2:5]) # Hello (end value is exclusive)
print(text[2:]) # Hello World , from index 2 to end
print(text[:5]) # Hello, from start to index 4
print(text[:]) # Hello World, from start to end
print(text[2:10:2]) # HloWrd, from index 2 to index 9, with step 2
print(text[:-2]) # Hello Wor, from start to end, excluding second last character
print(text[::-1]) # dlroW olleH, from start to end, with step -1
print(text[-1::-1]) # dlroW olleH, from end to start, with step -1

text  = "Hello"
print(text[-5:-5]) # ()
print(text[-5:-4]) # H , equivalent to: text[0:1]
print(text[-1:-3]) # ()
print(text[-1:-3:-1]) # lH # text[4:2:-1]


# 5: immutability
text = "apple"
# text[0:3] = "APP" # TypeError: 'str' object does not support item assignment
# text[0] = "A" # TypeError: 'str' object does not support item assignment

# 6: string methods
text = "Hello World"
print(text.upper()) # HELLO WORLD # All of these return new strings
print(text.lower()) # hello world
print(text.title()) # Hello World
print(text.capitalize()) # Hello world
print(text.swapcase()) # hELLO wORLD

# 7: string methods
text = "Hello World"
print(text.startswith("Hello")) # True
print(text.startswith("hello")) # False
print(text.endswith("World")) # True
print(text.endswith("world")) # False

# 8: string methods
text = "Hello World"
print(text.find("W")) # 6
print(text.find("w")) # -1
print(text.index("W")) # 6
# print(text.index("w")) # ValueError: substring not found

# 9: string methods
text = "Hello World"
print(text.count("l")) # 3
print(text.count("L")) # 0

# 10: string methods
text = "Hello World"
print(text.replace("World", "Universe")) # Hello Universe
# replace() does not modify the original string.
# Instead, it creates a new string and returns it.