'''pop-procedural oreinted programming
functions
def <funname>(parameters):
    """doc string"""
    statement(s)...
    .......body of fun
    return values(s)..
fanme(args)#func call
'''
def add(a,b):
    """addition function"""
    c=a+b
    return c
print(add(4,6))
c,d='codegnan','python'
print(add(c,d))
a,b=map(str,input('eneter the value').split(','))
print(add(a,b))
def addition(*a):
    """ using args as demo of variables length arguments"""
    print(a)
    print(type(a))
addition(1,2,3)
marks=[20,10,40,70]
addition(marks)
addition(*marks)
a,*b,c=1,2,'nsk',5.6,78
print(a)
print(b)
print(c)
def merge(*a):
    result=0
    for i in a:
        if(type(i) in [int,float]):
            result=result+i
    return result
print(merge(2,'codeganan',3,4))
def batch(name,age=21,place='vizag'):
    """keyword arguments usage"""
    print(f"{name} is in {place} and age is {age} years")
batch('codegnan',5,'hyderabad')
batch(place='vijayawada',name='codegnan',age=12)
batch('nsk')
print(4,5,sep=':')
def batch(**kwargs):
    """keyword variable length arguments usage"""
    print(kwargs)
    print(type(kwargs))
batch()
batch(name="akash",age=21,place="vizag",branch="cse")
data={'name':['nsk','sai'],'place':['vizag','hyderbad']}
data.update({'batch':'pfs-vsp-004'})
batch(**data)
#task using args and kwargs in one function
