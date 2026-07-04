"""
palindrome

a=input()
b=''
for i in a:
    b=i+b
print("it is palindrome" if a==b else "it isnot a palindrome")
#print(ifa==a[::-1])

fibnocii series

a,b=0,1
l=int(input())
print(a,b,end=" ")
for i in range(1,l):
    a,b=b,a+b
    print(b,end=" ")

calculator

a=int(input())
b=int(input())
user_in=int(input("enter\n1.add\n2.sub\n3.mul\n4.pow:"))
if user_in==1:
    print(a+b)
elif user_in==2:
    print(a-b)
elif user_in==3:
    print(a*b)
else:
    print(a**b)

tables


t=int(input())
for i in range(1,11):
    print(f"{t}x{i}={t*i}")

prefect number


n=int(input())
s=0
for i in range(1,n):
    if(n%i==0):
        s+=i
print("it is prefect number" if(n==s) else "it is  not prefect number")
        


"""

















