#polymorphism>>>method,operator overloading,method overriding
#poly-many,morph-forms
# hotstar >>> free users,premium users,vipusers
'''class Hotstar:
    """undewrstanding polymorphism"""
    def __init__(self):
        print("welcome to hotstar")
    def watch (self,*movie):
        self.movie=movie
        if movie==():
            print('movies list')
        else:
            print(f'user watching:')
            #for i in self.movie:
            #   print(f'{i},')
            print(*self.movie,sep="\n")
                
            
u1=Hotstar()
u1.watch()
u1.watch("leo",'vikram')

class Hotstar:
    """undewrstanding polymorphism"""
    def __init__(self):
        print("welcome to hotstar")
    def movies_list(self,content):
        self.content=content
        if isinstance(content,str):
            print(f"user watching {self.content}")
        elif isinstance(content,list):
            print(*content,sep='\n')
u1=Hotstar()
u1.movies_list('hi guys')
u1.movies_list(['hello','hi','bye'])

class Hotstar:
    """undewrstanding polymorphism"""
    def __init__(self):
        print("welcome to hotstar")
    def movies_list(self,content):
        self.content=content
        if isinstance(content,str):
            #print(f"user watching {self.content}")
            print("can watch free content with advertisement")
        elif isinstance(content,list):
            #print(*content,sep='\n')
            print("can watch premium content without advertisments")
        else:
            print("can watch premium content along with devices count,streaming")
class users(Hotstar):
    def movies_list(self):
        super().movies_list('')
        
#u1=Hotstar()
#u1.movies_list('hi guys')
#u1.movies_list(['hello','hi','bye'])
u1=users()
u1.movies_list()


class Hotstar:
    def watch(self):
        print('welcome to hotstar')
class freeusers(Hotstar):
    def watch(self):
        super().watch()
        print('free users')
class premiumusers(freeusers):
    def watch(self):
        super().watch()
        print('premium users')
class vipusers(premiumusers):
    def watch(self):
        super().watch()
        print('vip users')
u1=vipusers()
u1.watch()


class Hotstar:
    """undewrstanding polymorphism"""
    movies=['raaka','pradise','varanasi','spirit']
    def __init__(self):
        print("welcome to hotstar")
    def movies_list(self):
        print(movies)
    def advertisments(self):
        print("adddddd")
        
class users(Hotstar):
    def movies_list(self):
        super().movies_list()

class premiumusers(Hotstar):
    def movies_list(self):
        super().movies_list()

class vipusers(Hotstar):
    def movies_list(self):
        super().movies_list()
        

u1=users()
u1.movies_list()


a=13;b=24
print(a<=b)
print(a.__le__(b))
print(a+b)
print(a.__add__(b))
print("rocky".__add__('bhai'))
a=[1,2,3,4,5]
print(a.__len__())

'''

class watchhistory:
    def duration(self,hours):
        self.hours=hours
    def __add__(self,other):
        return self.hours+other.hours
    def __str__(self):
        print(f"watching history is {self.hours}")
u1=watchhistory()
u1.duration(25)
u2=watchhistory()
u2.duration(35)
print(u1.__add__(u2),u1+u2,u1.hours+u2.hours)
u1.__str__()














