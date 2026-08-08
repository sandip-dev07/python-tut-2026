a = 10;

def func():
    print(globals()['a'])
    globals()['a'] = 30
    a = 20
    print("inside function",a)

func()
print("outside function",a)


#  factorial:
x :int = 5

def fact(x: int):
    if x == 0:
        return 1
    return x * fact(x-1)

print(fact(120))