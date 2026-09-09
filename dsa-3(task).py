#task using args and kwargs in one function
#student marks and average

def _student_(*args,**kwargs):
    """enter 'first marks' and 'next student details'"""
    print(f'Name:{kwargs["name"]}\nBranch:{kwargs["branch"]}')
    print(f'total marks:{sum(args)}')
    print(f'average marks:{sum(args)/len(args)}')

stud_dict={"name":input("enter name:"),"branch":input("enter branch:")}

print("enter marks:")
_student_(int(input("softskils:")),int(input("Aptitude:")),
          int(input("Python:")),int(input("MySQL:")),**stud_dict)
