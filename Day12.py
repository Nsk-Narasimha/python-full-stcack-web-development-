"""functions
biult in (print(),max(),type(),int()...etc)
userdefined functions-starts with def keyword
def function_name(parameters):
  .........
      .........
          ........
functinname(arguments)
types of arguments:
required arguments,default,keyword,variable length



def add():
    print("he;llo")
add()
"""
def add(a,b):
    print(a+b)
add(4,5)
def add(a,b=5):
    print(a+b)
add(4,7)
def add(a,b):
    print(a)
add(b=7,a=4)
def add(*a):
    print(a[0],a)
add(6,4,7)
def add(*a,**b):
    print(b["a2"])
add(a1="nsk",a2=18)
a=5
def add():
    global b
    a=1
    b=2
    c=9
    print(a+b+c)
b=7
add()
print(a,b)
