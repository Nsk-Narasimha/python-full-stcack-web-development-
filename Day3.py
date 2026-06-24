#data types
#int
n=8
#float
n=5.61
'''string
it is sequence of char that are enclosed in ' '," ",""" """
it is immutable
concatination-"+"
'''
so="python"
any_="is a high level language"
print(so+any_)
#indexing
print(so[2])
print(so[-2])
"""methods
replace()-variablename.replace("old string","newstring",count)
join()
split()
count()-variable.count("substring",strat index,end index)
biultin functions
len()
max()
min()
lower()
upper()
strip()
"""
print(any_.replace('a','A',2))
print(",".join(so))
print(any_.split(' a '))
print(any_.split('a'))
print(any_.count('a',5,50))
print(len(so))
print(max(any_))
print(min(any_))
