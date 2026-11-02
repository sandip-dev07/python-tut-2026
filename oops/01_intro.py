

a = 18;
print(type(a)) # <class 'int'> : this is a class type integer
print(a.bit_length())



class computer:
    
    def config(self):
        print("i5, 16gb, 1tb")
 
comp1 = computer()
print(type(comp1)) # <class '__main__.computer'> : this is a class type computer
comp1.config()

comp1.webcam = "Logitech"
print(comp1.webcam)

# comp2 = computer()
# comp2.config()