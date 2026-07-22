"""errors
------------
syntax error:
for i in range(1,10:
    print(i)

indentation error:
    a=20
for i in range(1,10):
print(i)

value error:
name=int(input("enter name:"))

name error:
print(num)

error handling
--------------
try:
except:
else:
finally:

"""
try:
    #print(num)
    #print(int(input("enter name:")))
    print(9/0)
except NameError:
    print("it is name error")
except ValueError:
    print("value error")
except ZeroDivisionError:
    print("ZeroDivisionerror")
else:print("no errors")
finally:print("end")










    
