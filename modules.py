#employee details
def employees(*names,**settings):
    """employee names and details"""
    print("Employee names")
    for employee in names:
        print('--------')
        print('-',employee)

    for key,value in settings.items():
        print("key is",key)
        print("value is",value)
'''employees("dinesh","sanjay","sai",
          dept="software",
          exper=True,
          salary=True)'''
details={'organization':'Codeganan','year':2008
         ,'branches':['vijaywada','hyderbad','vizag']}
print(__name__)
