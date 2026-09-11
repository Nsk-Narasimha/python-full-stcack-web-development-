"""
package

colletion classes,function is module(reusable,organized code)

organiztion=>class(attributes,methods)
encapsulation,inheritence,polymorphism

employees-->function
performance metrics-->fuction
increment-->function

emp1,e2,e3>>>>objects
"""
import modules
print(dir(modules))
'''print(type(modules.details))
print(type(modules.employees))
modules.employees('narasimha',designation="student",
                  location="vizag")
print(modules.details.keys())
print(modules.details['organization'])
modules.details.update({'batches':['pfs','jfs','da','aaa','ds'],
                        'employees':240})
print(modules.details)'''
from modules import employees,details
details.update({'batches':['pfs','jfs','da','aaa','ds'],
                        'employees':240})
print(details)
print(modules.__doc__)

print(__doc__)
#biult in modules-->math,random,os,time,datetime
#we downlod modules-->pypi(python package index)
#biuld a qrcode  scanner using python -->linkedin url
#pyqrcode,pypng(pypi.org)
import pyqrcode,png
#create a qrcode by giving a link
link="https://www.linkedin.com/in/narasimha-sai-kumar-kosuri-a48695289/"
qr=pyqrcode.create(link)
print(qr)
qr.png("myqr.png",scale=100)

