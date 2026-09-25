g=[i for i in range(1,21) if i%2==0]
print(g)
def even(b):
    result=[]
    for i in range(0,b):
        
        if(i%2==0):
            result.append(i)
    return result
print(even(-15))

h=list(filter(lambda i:i%2==0,range(1,21)))
print(h)
k=list(filter(lambda x:len(x)>=5, ["Sai", "Kumar", "Ravi", "Narasimha"]))
print(k)
k=list(map(lambda x:len(x)>=5 , ["Sai", "Kumar", "Ravi", "Narasimha"]))
print(k)
'''
j=list(map(int,input().split()))
print(j)
a,b=list(map(int,input().split(',')))
print(a,b)
name,place=input().split()
print(f'name:{name},place:{place}')
name,place=map(str,input().split())
print(f'name:{name},place:{place}')
'''
names=list(map(lambda x:x.upper(),["Sai", "Kumar", "Ravi", "Narasimha"]))
print(names)
prices=[2500,3500,5000,7500]
print(list(map(lambda x:x-(x*(10/100)),prices)))
print([i**2 if(i%2==0) else i for i in range(1,21) ])
print([(i,j) for i in ['green','blue','red'] for j in ['s','m','l']])
marks=[25,25,24,20]
weekly=[35,30,45,48]
print(list(map(lambda m,w:m+w,marks,weekly)))

f=[i+4 if i>=j else i-3 for i in range(1,5) for j in range(1,5)]
print(f)














