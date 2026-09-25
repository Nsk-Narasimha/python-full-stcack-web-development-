'''
abstraction

import abc
#print(dir(abc))
from abc import ABC,abstractmethod
print(help(ABC),help(abstractmethod))
class content(ABC):
    @abstractmethod
    def upload(self):
        pass
class photo(content):
    def upload(self):
        print("""photo successfully uploded
photo is compressed and  edited as per filters choosen
photo is posted""")
class video(content):
    def upload(self):
        print("""video successfully encoded
video is compressed and  edited as per filters added
video is posted with filters """)
class reel(content):
    def upload(self):
        print("""reel edited with music
reel is compressed and  edited as per filters choosen
reel is edited and posted succesfully""")
contents=[photo(),video(),reel()]
for con in contents:
    con.upload()'''
#list comperhension
'''l=[3,4,5,6,7]
for i in l:
    l.extend([i**2])
print(l)'''
l=[]
for i in range(10):
    l.append(i)
    #l.extend([i,])
print(l)
l=[i for i in range(10)]
print(l)
l=[i**2 for i in range(5)]
print(l)
data=['codegnan','nsk','saketh']
new_data=[i.upper() for i in data]
print(new_data)










    
