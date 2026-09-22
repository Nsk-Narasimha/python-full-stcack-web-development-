'''
inheritance

single,multiple,multi level,hierarchical,hybrid

class Users:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def fullname(self):
        return f'{self.fname+" "+self.lname}'
class Update_Users(Users):
    def update(self):
        self.fname=self.fname.title().strip()
        self.lname=self.lname.title().strip()
        return self.fullname()

        
u1=Users('nsk','k')
print(u1.fullname())
u2=Update_Users('nsk','k')
print(u2.update())


#class method '@'
class Rbi:
    cash=10000000000000000
    @classmethod
    def rbi_cash(cls):
        return f'available cash with rbi is {cls.cash}'
class Hdfc(Rbi):

    camount=500000
    @classmethod
    def hdfcc_cash(cls):
        return f'available cash with rbi is {cls.cash} and hdfc is {cls.amount}'
print(Rbi.rbi_cash())
print(Hdfc.hdfcc_cash())
print(Rbi.rbi_cash())
 
#using constructor
class Father:
    def __init__(self):
        self.fproperty=2500000
        
    def father_property(self):
        print(f'father property is {self.fproperty}')
class Kid(Father):
    def __init__(self):
        super().__init__()
        self.kproperty=500000
        #super().__init__()
    def kid_property(self):
        print(f'kid property is {self.kproperty}')
        print(f'kid and father combined property is {self.kproperty+self.fproperty}')
k=Kid()
print(k.kproperty)
k.father_property()
k.kid_property()
'''





























