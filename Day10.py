"""
prime user input,generating prime number how many,for that number

m=int(input())
c=0
for i in range(2,m):
    if(m%i==0):
        c+=1
if(c==0):print(f"{m} is prime number")
else:print(f"{m} is not prime number")
print(f"below {m}, primes are:")
n=2
while(n!=m):
    c=0
    for i in range(2,n):
        if(n%i==0):
            c+=1
    if(c==0):
        print(n,end=' ')
    n=n+1
print(f"\nfirst {m} numbers are:")
n=2
co=0
while(co!=m):
    c=0
    for i in range(2,n):
        if(n%i==0):
            c+=1
    if(c==0):
        print(n,end=' ')
        co+=1
    n=n+1
"""
"""
star patterns

n=int(input())
for j in range(n):
    for i in range(j+1):
        print("*",end="")
    print()
for j in range(n):
    for i in range(1,(n+1)-j):
        print("*",end="")
    print()

for j in range(n):
    for i in range(1,n-j):
        print(" ",end="")
    for i in range(j+1):
        print("*",end="")
    print()
for j in range(n):
    for i in range(j):
        print(" ",end="")
    for i in range(1,(n+1)-j):
        print("*",end="")
    print()
for j in range(n):
    for i in range(1,n-j):
        print(" ",end="")
    for i in range(j+1):
        print("* ",end="")
    print()

for j in range(n):
    for i in range(j):
        print(" ",end="")
    for i in range(1,(n+1)-j):
        print("* ",end="")
    print()
    
Arm strong number
n=input()
c=0
for i in n:
    c+=int(i)**len(n)
print(c)
"""
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i):
        print(i-j,end="")
    print()
    
