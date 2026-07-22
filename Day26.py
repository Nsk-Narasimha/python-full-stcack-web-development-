""" file handling
file to be create,update

two ways to open:
1.open()
do=open('file_name','mode')
close()

2.with(keyword)
with open('file_name','mode')as do:

methods:
write():this function is used to add the text inside  a file or update a file with new text
read():read allfile at once
readline():read one line at a time
readlines(): it store as list of lines

"""
do_=open('1.py','r')#read
print(do_.read())

with open('mysql\\mysqlclassnotes\\day1.txt','r')as do:
    print(do.read())
    
with open('day27.py','w')as do:#write from start of deleteing old contenet or if not exist it creates 
    print(do.write("n=int(input())"))

with open('day27.py','a')as do:#write at end  text already there in it
    print(do.write("\nprint('even' if(n%2==0) else 'odd')"))


with open('day27.py','r')as do:#it goes cursor at end that's why it was not performing next read and readline
    print(do.readlines())
    print(do.readline())
    print(do.read())
    
    
with open('day27.py','x')as do:#new create if exist throughs error
    print(do.write("n=int(input())"))
