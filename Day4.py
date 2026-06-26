"""
list data types
collection of different data type that are enclosed in []

>>mutable,,,,,,,,,,immutable
modified           can't be modified
list               strings

methods:
1.append()-add to last index osition
2.extend()
3.pop()
4.remove()
5.insert()
"""
s="sai"
l=["nsk",3.14,[1,2]]
print(l)
l.append(1)
print(l[::-1])
l.append([10,20])
l.extend([30,40])
print(l)
l.append('sai')
l.extend('sai')
print(f"{l}\n{len(l)}")
so_=[1,2,'python is a language',[45,78,"java is a language",[1,23],90],"hello"]
print(so_)
print(so_[3][2][10])
print(so_[3][3][1])
print(l.pop(-4))
print(l)
print(l.remove("s"))
print(l)
l.insert(3,55)
print(l)
l1=[56,[1,2],['python','java',['python is a language',153,90],[78,6],'i know c']]
print(l1[2][2][1])
print(l1[2][4][2:6])
print(l1.count(56))
l1.insert(2,99)
print(l1)
"""
tuple
collection of different data types represent in ()
immutable
method :index,count
"""
t=(1,2,3,4,"python",[4,5],(90,78))
print(t.index('python'))
l2=[4,6,2,9,1]
print(sorted(l2))
print(l2)
l2.sort()
print(l2)




