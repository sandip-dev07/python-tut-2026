# Inner funcion: 

def outer():
    print("outer function")
    a:int = 10
    
    def inner():
        print("inner function")
        b:int = a + 20
        print(b)
    
    # inner()
    return inner

# outer()
inner = outer()
inner()