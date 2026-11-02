

class Example:
    
    def __new__(cls):
        print("new called")
        return super().__new__(cls)
    
    def __init__(self):
        print("init called")
        
    def show(self):
        print("show called")
        

# ex = Example()
# ex.show()

ex2 = Example.__new__(Example)
ex2.show()



# __new__ → object creation
# __init__ → object initialization

# Student("Sandip")
#        │
#        ▼
# ┌─────────────────┐
# │    __new__()    │
# │                 │
# │ Creates object  │
# └────────┬────────┘
#          │
#          │ returns object
#          ▼
# ┌─────────────────┐
# │    __init__()   │
# │                 │
# │ Initializes it  │
# └────────┬────────┘
#          │
#          ▼
#        s1


# You usually don't need __new__.
# __new__ becomes useful when you need to control object creation itself.

# __new__ is responsible for creating and returning a new instance, while __init__ is responsible for initializing that already-created instance. __new__ receives cls, whereas __init__ receives self. __new__ is mainly used when we need to control object creation, such as with immutable types or singleton patterns.