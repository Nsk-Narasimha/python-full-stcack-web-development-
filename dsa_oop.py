'''
oop-object oriented programming>>class and objects
pop-procedure oriented programming>>functions
 class is a blueprint of a object
 object -->attributes(variables),methods(functions)
 as encapsulation,inheritance,polymorphisam

class ClassName:
    """ doc String"""
    #attributes (define the data)
    ............
    def fname(self):
    def __init__(self):
        statements...........
obj=ClassName()

class Students:
    """students details"""
    name="akash"
    age=20
    place="vizag"
    def details(self):
        print(f'{self.name} is in {self.place} and age of {self.age} years')

st=Students()
print(st)
print(dir(st))
print(st.name,st.age,st.place)
print(st.details())

class Students:
    def details(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(f'student name is {self.name}')
        print(f'student age is {self.age} and lives in {self.place}')
st=Students()
st.details("nsk",22,"viazg")
print(st.name,st.place)
st.display()
print(st.__class__)
print(st.__doc__)
print(st.__dict__)
'''
class Students:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def __add__(self,st):
        print(self.age+st.age)
    def display(self):
        print(f'student name is {self.name}')
        print(f'student age is {self.age} and lives in {self.place}')
st=Students("nsk",22,"viazg")

print(st.name,st.place)
st.display()
print(st.__dict__)
st2=Students("sai",50,"beach")
print(st2.__dict__)
st+st2

class Cars:
    def __init__(self,brand,name,price):
        self.brand=brand
        self.name=name
        self.price=price
    def display(self):
        print(self.brand,self.name,self.price)
c1=Cars("audi","vxi2",9999999)
c1.display()
print(c1.__dict__)
#encapsulation
class Users:
    def __init__(self,username,_otp,password):
        self.user=username#public
        self._otp=_otp#protected
        self.__password=password
    def display(self):
        print(f'username is {self.user}')
        print(f'otp is {self._otp} ,{self.__password}')
u1=Users("nsk",6789,"admin123")
u1.display()
print(u1.user)
u1.user="sam"
u1._otp=4567
u1._Users__password="admin456"#after get,set methods
u1.display()
print(u1.__dict__)










