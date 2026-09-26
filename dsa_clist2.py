b=[i for i in range(1,10) if i>4]
print(b)
print(type(b))
b=(i for i in range(1,10) if i>4)
print(b)
print(type(b))
def details():
    return f'codegnan is vizag'
    return "nsk"
print(details())
def details():
    a=10
    yield f'codegnan is vizag,{a}'
    a=20;b=30
    yield f"nsk{a,b}"
print(details())
detail=details()
#print(*detail)
#print(next(detail))
#print(next(detail))
for i in detail:
    print(i)
    #print(next(i))-error
b=(i for i in range(1,10) if i>4)
print(b)
for i in b:print(f"values is:{i}")
a,b=3,4
a,*b,c=3,"codeganan","python",5,78,"vizag"
print(a,b,c)

"""exception handling
try except finally

while True:
    try:
        a,b=map(int,input("enter the values").split())
        c=a/b
        print(c)
        break
    except ZeroDivisionError:
        print("make sure the denominator value is only +ve/-ve not zero")
    except TypeError:
        print("type error")
    except NameError:
        print("sarigaa chusukoo")
    except Exception as e:
        print(e)

try:
    a=[3,4,5,2,1]
    print(a[4])
    a.append("nsk")
    print(a)
except IndexError:
    print("check the element count properly")
except AttributeError:
    print("do check the method names properly")
finally:
    print("its done")

try:
    a=[3,4,5,2,1]
    print(a[4])
    a.append("nsk")
    print(a)
except (IndexError,AttributeError,NameError) as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print("its done")

"""
#file handling -->r-->read(),w-->write(),a,r+....
#with kayword usage
with open("hfile.txt",'r+') as f:
    #print(f.read())
    #f.write("using with keyword")
    f.write("hi guys")
    print(*f)



















