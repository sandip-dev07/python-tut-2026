
class Computer:
    # def __init__(self): 
    #     print("inside constructor")
        
    def __init__(self, cpu, ram, hdd): # constructor # slef: current object itself, you may say 'this'
        print("inside constructor")
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd
        
    def config(self):
        print(self.cpu, self.ram, self.hdd)
        
        
        
comp1 = Computer("i5", 16, 1)
comp1.config()

comp2 = Computer()
comp2.config()



# Python does not support constructor overloading. The second __init__() replaces the first one.