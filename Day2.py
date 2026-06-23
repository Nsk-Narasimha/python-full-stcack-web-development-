'''
operators
--------
1.arithmetic
2.assignment
3.comparsion
4.logical
5.identity
6.membership
7.bitwise
'''
#arithmetic:+,-,*,/,//,**,%
a,b=5,2
print(a+b,a-b,a*b,a/b,a//b,a**b,a%b)
#assignment:=,+=,-=,*=,/=,%=
a+=1
print(a)
#comparsion:>,<,<=,>=,==,!=
print(a>=b)
#logical:and,or,not
print(a==5 and b==2)
print(a==5 or b==2)
print(not a!=b)
#identity:is,is not
c=3
d=3
print(id(c))
print(id(d))
print(c==d)
print(c is d)
c,d=[1,2],[1,2]
print(id(c))
print(id(d))
print(c==d)
print(c is d)
#membership: in,not in
print(b in c)
#bitwise:&,\,^,>>,<<
print(a,b,a^b)
