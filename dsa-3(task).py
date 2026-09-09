#task using args and kwargs in one function
#student marks and average

def _student_(*args,**kwargs):
    """enter 'first marks' and 'next student details'"""
    print(f'Name:{kwargs["name"]}\nBranch:{kwargs["branch"]}')
    print(f'total marks:{sum(args)}')
    print(f'average marks:{sum(args)/len(args)}')
    
_student_(40,60,50,70,name='nsk',branch='cse')
