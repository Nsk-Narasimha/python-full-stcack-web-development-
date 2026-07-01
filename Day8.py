"""
statements
1.conditions
*if
*if else
*elif
2.control
*break
*continue
*pass
3.loop
*for
*while
______________
n=int(input("enter a number:"))
if n%2==0:print(f"{n} is even number")
else:print(f"{n} is odd number")
--------
m=int(input("enter your marks"))
if(m>=90):print("A+")
elif(m>=80):print("A")
elif(m>=70):print("B+")
elif(m>=60):print("B")
elif(m>=50):print("C")
elif(m>=40):print("D")
elif(m>=30):print("E")
else:print("Fail")
-------
n1,n2,n3=map(int,input("enter three numbers with spaces").split())
if(n1>=n2 and n1>=n3):print(f"{n1}is max number")
elif(n2>=n1 and n2>=n3):print(f"{n2}is max number")
else:print(f"{n3}is max number")
"""
c=input("eneter character")
if c in "AEIOUaeiou":
    print(f"'{c}' is vowel")
else:
    print(f"'{c}' is consanant")
