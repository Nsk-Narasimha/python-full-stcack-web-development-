# Ploymorphism: Ploymorphism means many form.
#           ->  It allows same method, function or operator to perform different tasks depending on the same object.

# Types:

# 1. Method Overloading: Method overloading means having multiple methods with the same name but different parameters.

class Cal:
    def add(self,num,num_2=0):
        print(num+ num_2)
    def sub(self,num,num_2=0):
        print(num - num_2)
obj= Cal()
obj.add(3,7)
obj.sub(7,2)

class Cal:
    def add(self,num,num_2=0):
        print(num + num_2)
    def mul(self,a,b):
        print(a*b)
obj= Cal()
obj.add(45,20)
obj.mul(4,5)

class Cal:
    def add(self,num,num_2):
        print(num + num_2)
    def add(self,num,num_2,num_3=0):
        print(num+num_2+num_3)
obj= Cal()
obj.add(10,20)
obj.add(4,5,251)

# 2. Method Overriding: The method Overriding occurs when a child class provides its own implementation of a method
#                       already defined in its parent class.

class animal:
    def sound(self):
        print("Animals make sounds")
class dog(animal):
    def sound(self):
        print("Dogs barks")
d= dog()
d.sound()

# 3. Operator Overloading: This allows operators such as +,-,* to work differently for user-defined objects.

# --> __add__ (+)

# --> __sub__ (-)

# --> __mul__ (*)

class student:
    def __init__(self,marks):
        self.marks= marks
    def __add__(self,other):
       return self.marks - other.marks
s1= student(30)
s2= student(20)
print(s1+s2)

class student:
    def __init__(self,marks):
        self.marks= marks
    def __sub__(self,other):
       return self.marks + other.marks
s1= student(30)
s2= student(20)
print(s1-s2)

class student:
    def __init__(self,marks):
        self.marks= marks
    def __mul__(self,other):
       return self.marks - other.marks
s1= student(30)
s2= student(20)
print(s1*s2)














