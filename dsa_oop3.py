'''
usage of super()
super with arguments-->super().__init__(args)

class Father:
    def __init__(self,fproperty):
        self.fproperty=fproperty
        
    def father_property(self):
        print(f'father property is {self.fproperty}')
class Kid(Father):
    def __init__(self,kproperty,fproperty):
        super().__init__(fproperty)
        self.kproperty=kproperty
        
    def kid_property(self):
        print(f'kid property is {self.kproperty}')
        print(f'kid and father combined property is {self.kproperty+self.fproperty}')
k=Kid(50000000,25000000)
k.kid_property()


class Square:
    def __init__(self,x):
        self.x=x
    def area(self):
        return f'area of square({self.x}):{self.x*self.x}'

class Rectangle(Square):
    def __init__(self,y,x):
        self.y=y
        super().__init__(x)
    def area(self):
        
        return f'{super().area()}\narea of rectangle{self.x,self.y}:{self.x*self.y}'
        
#o1=Rectangle(7,8)
#print(o1.area())
#o2=Square(7)
#print(o2.area())
x,y=map(int,input("enter values").split(' '))
o3=Rectangle(x,y)
print(o3.area())

class users:
    def voice_call(self):
        print("userss can make vpoice call")
class notifications:
    def send_notifications(self):
        print("user can get pop-up notifications")
class premiumusers(users,notifications):
    def verification_badge(self):
        print("user is verified and bluetick added")
u1=premiumusers()
u1.verification_badge()
u1.voice_call()
print(dir(u1))

class users:
    def voice_call(self):
        print("userss can make vpoice call")
class notifications:
    def send_notifications(self):
        print("user can get pop-up notifications")
class businessusers(users,notifications):
    def create_catlog(self):
        print("details added successfully")
class premiumusers(businessusers):
    def verification_badge(self):
        print("user is verified and bluetick added")
u1=premiumusers()
u1.verification_badge()
u1.voice_call()
u1.create_catlog()
print(dir(u1))



class animal:
    def sounds(self):
        print("animal sound is:",end='')
class dog(animal):
    def sounds(self):
        super().sounds()
        print("bow bow")
class cat(animal):
    def sounds(self):
        super().sounds()
        print("meow meow")
d=dog()
d.sounds()
c=cat()
c.sounds()

class amozon():
    def products(self):
        print("products you bought:",end='')
    def addproducts(self):
        print("you added items:",end='')
class users(amozon):
    def buy(self,*args):
        super().products()
        print(*args)
class shop(amozon):
    def add(self,*args):
        super().addproducts()
        print(*args)
#u1=users()
#u1.buy("toy car","bat","curtain")
s1=shop()
s1.add("toys")
'''
#polymorphism>>>method,operator overloading,method overriding
#poly-many,morph-forms
# hotstar >>> free users,premium users,vipusers
class Hotstar:
    """undewrstanding polymorphism"""
    def watch(self):
        print("user logged in and surfing basic content")
    def watch (self,movie):
        self.movie=movie
        print(f'user watching{self.movie}')
u1=Hotstar()
u1.watch("leo")











