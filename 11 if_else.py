age = 44

if age <= 18:
    print("You are a child")
elif age >= 65:
    print("You are a senior")
else:
    print("You are an adult")
    


num  = 50

if (num & 1) :
    print("Odd")
else:
    print("Even")
    
    
# switch renamed as match in python 3.10
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _: # default
        print("Invalid day")