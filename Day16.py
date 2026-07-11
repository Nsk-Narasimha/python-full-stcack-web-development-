"""
generator
"""
def some():
    yield 1
    yield 2
    yield 3
    return 1
so=some()
print(so)
print(next(so))
print(next(so))
print(next(so))

def demo():
    print("start")
    yield 
    print("middle")
    yield 2
    print("end")
    yield 3
so=demo()
print(so)
print(next(so))
print(next(so))
print(next(so))
def how(so):
    fot i in range (so):
        yield i*i

so=demo(5)
print(so)
print(next(so))
print(next(so))
print(next(so))
print(next(so))
print(next(so))
def how(so):
    fot i in range (so):
        print( i*i)
how(4)
gen=(x*x for x in range(5))
print(next(gen))
print(next(gen))
