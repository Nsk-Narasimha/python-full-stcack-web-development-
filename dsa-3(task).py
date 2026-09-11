#task using args and kwargs in one function
#student marks and average

def _student_(*args,**kwargs):
    """enter 'first marks' and 'next student details'"""
    for key,value in kwargs.items():
        print(f"{key}:{value}")
    
    print(f'total marks:{sum(args)}')
    print(f'average marks:{sum(args)/len(args)}')

stud_dict={"name":input("enter name:"),
           "branch":input("enter branch:")}
print("enter marks:")
stud_marks=[int(input("softskils:")),int(input("Aptitude:")),
          int(input("Python:")),int(input("MySQL:"))]
              
_student_(*stud_marks,**stud_dict)


