
class Computer:
    
    brand = "Dell" # class variable

        
    def __init__(self, cpu, ram, hdd): # constructor # slef: current object itself, you may say 'this'
        print("inside constructor")
        self.cpu = cpu # instance variable
        self.ram = ram
        self.hdd = hdd
        
    def config(self):
        print(self.cpu, self.ram, self.hdd)
      
    @classmethod  
    def info(self): # A class method receives the class itself as the first argument.
        print(self.brand)
        
    @staticmethod
     # It's basically a normal function placed inside the class because it logically belongs there.
    def is_even(number):
        return number % 2 == 0
        
        
        
comp1 = Computer("i5", 16, 1)
comp1.config()

comp2 = Computer("i7", 32, 2)
comp2.config()

print(Computer.info()) # class method



# ------------------------------------------------

class BankAccount:

    bank_name = "SBI"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # Object-specific
    def deposit(self, amount):
        self.balance += amount

    # Class-specific
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    # Utility function
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0