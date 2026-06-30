"""
input formatting from user

input()-take input from user


n1=int(input("enter first number"))
n2=int(input("enter second number"))
print(n1+n2)
s=input("enter your name")
print(s)
f1=float(input("enter decimal value"))
print(f1)
l1=list(map(int,input().split(',')))
print(l1)
l=list(input())
print(l)
t1=tuple(map(int,input().split()))
t2=tuple(input().split())
print(t1,t2)
e=eval(input("enter"))
print(type(e),id(e),e)
e1=list(map(eval,input("enter:").split()))
print(e1)
"""
a,b=map(int,input().split())
print(f"{a}+{b}")
print("%d+%d"%(a,b))
print("{0}+{1}".format(a,b))

