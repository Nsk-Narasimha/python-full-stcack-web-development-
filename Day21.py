"""self keyword"""
class test:
    def display(self):
        print(self)
t=test()
print(t)
t.display()
"""constructor"""
class batch:
    def __init__(self,name,branch,age):
        self._name=name#protected
        self.branch=branch#public
        self.__age=age#private
    def display(self):
        
        print(self._name,self.branch,self.__age)
d =batch('nsk','cse',14)
d.display()
print(d._name,d.branch,d._batch__age)
"""encapsulation"""
class atm:
    def __init__(self,balance):
        self._balance=balance
    def deposit(self,amount):
        self._balance+=amount
        print(self._balance)
a=atm(700)
a.deposit(800)

class car:
    @classmethod
    def cars(self,name,color):
        print(name,color)
car.cars("toyata","red")
