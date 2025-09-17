class calculation:
    def add(self,a,b):
        return a+b
    
    def subtract(self,a,b):
        return a-b
    
    def product(self,a,b):
        return a*b
    
    def divide (self,a,b):
        return a/b

class word:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def show(self):
        print(self.add())
        print(self.subtract())
        print(self.product())
        print(self.divdie())