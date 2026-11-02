import sys
from time import sleep

sys.setrecursionlimit(100)
print(sys.getrecursionlimit())

count = 1

def greet():
    global count
    print("Hello", count)
    count = count + 1
    sleep(0.3)
    greet()

greet()