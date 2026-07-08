""" passing by value

def some(a):
    for j in a:
        print(j)
some("qweqfw")

passing by reference

def some(a):
    print(a)
    a.append(4)
    print(a)
b=[1,2,3]    
some(b)
print(b)

return keyword
def add5(b):
    return 5+b
print(add5(5))
print(add5(15))

built in function-150


import builtins
b=[n for n in dir(builtins)
   if callable(getattr(builtins,n))]
print(b,len(b))

recursive function


def fact(n):
    if(n==1):return 1
    return n*fact(n-1)
print(fact(int(input())))
           
"""


























