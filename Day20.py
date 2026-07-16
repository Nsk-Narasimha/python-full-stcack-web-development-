#OOP's
'''---------------------------------

--->Object -Oriented programming system (OOP's),This will be organize the code using classes and object.

Use:-
------
1)Code reusable
2)East Maintance
3)Clear understanding
4)Better Security


*Classes
---------
-->Class is a blue-print or a template used to create an object...

class Batch_4:
     pass

*Object
---------
-->Object is a instance of the class

Example:

class student:
    studn = 'Manoj'
st_ = student()
print(st_)

Attributes
------------
-Attributes are the variable that belongs to an object or the class
*Example:-

1)class how:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def nam(self):
        print(self.name)
s1 = how('Manoj',55)
print(s1.nam())

2)
class how:
    def details(self,name,age):
        self.name = name
        self.age = age
        
s1 = how()
s1.details('Manoj',55)
print(s1.name)
print(s1.age)

*Methods
---------
--->Methods are nothing but,the functions inside the class


class Calculator:
    def add(self,num,num_2):
        print(num + num_2)
        
    def sub(self,num,num_2):
        print(num - num_2)

    def mul(self,num,num_2):
        print(num * num_2)
cal = Calculator()
cal.add(41,7)
cal.sub(27,7)
cal.mul(10,7)
'''
class how:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def nam(self):
        print(self.name)
s1 = how('Manoj',55)
print(s1.nam())
