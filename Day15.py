"""l=[4,4,5,6,6,6,7]
def s(l):
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    print(l1)
s(l)
def prime(n):
    c=0
    for i in range (2,n):
        if(n%2==0):
            c+=1
    if(c==0):print(f"{n} is prime")
    else:print(f"{n} is not prime")
prime(int(input("enter a number:")))
def leng(s):
    c=0
    for i in s:
        c+=1
    print(f"length is :{c}")
leng(input().split())

"""
s="python is A Programming languagE"
def countt(s,cap=0,smal=0,spac=0):
    for i in s:
        if i.isupper():cap+=1
        elif i.islower():smal+=1
        else:spac+=1
    print(f"capitals are:{cap}\nsmalls are:{smal}\nspaces are:{spac}")
countt(s)
