"""
Dictionary
dict is a keys:values pairsseprated by , and keys are unique/immutable data types
methods
keys()
values()
items()
update()
clear()
"""
d={"name":"teja",1:"numder",(6,7):[1,2]}
print(f"\n{d}\n{d.keys()}\n{d.values()}\n{d.items()}")
print(d["name"],d[1],d[(6,7)])
d.update({"name":"nsk",(6,7):7})
print(d)
d.clear()
print(d)
"""
set
collection of unordered element
set is mutable
remove duplicate by itself
methods:
union()-|
intersection()-&
symmetric_difference()-^
add()
remove()

"""
s={1,2,3,4,2}
s1={4,5,6,7}
print(s|s1)
print(s.union(s1))
print(s)
print(s&s1)
print(s.symmetric_difference(s1))
s.add(5)
s.remove(3)
print(s)
s.discard(2)
s.discard(7)
print(s)























