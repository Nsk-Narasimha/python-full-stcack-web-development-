'''n_of_t_user_input=int(input("enter the values"))
for i in range(n_of_t_user_input):
    weight=float(input("enter the weight in kgs:"))
    height=float(input("enter the height in meters:"))
    name=input('enter your name:')
    if(weight,height>0):
        bmi=weight/(height**2)
        print(f"Name:{name},height:{height},weight:{weight}, based on that your bmi value is {bmi}")
        if(bmi<18.5):print("underweight")
        elif(bmi<25):print("normal/healthy")
        elif(bmi<30):print("overweight")
        elif(bmi<35):print("obesity-class1")
        elif(bmi<40):print("obesity-class2")
        else:print("obesity-class3/severe obesity")
    else:print("make sure to enter only +ve values")
'''
n_of_t_user_input=int(input("enter the values"))
while(n_of_t_user_input):
    try:
        weight=float(input("enter the weight in kgs:"))
        height=float(input("enter the height in meters:"))
        name=input('enter your name:')
        if(weight>0 and height>0):
            bmi=weight/(height**2)
            print(f"Name:{name},height:{height},weight:{weight}, based on that your bmi value is {bmi}")
            if(bmi<18.5):print("underweight")
            elif(bmi<25):print("normal/healthy")
            elif(bmi<30):print("overweight")
            elif(bmi<35):print("obesity-class1")
            elif(bmi<40):print("obesity-class2")
            else:print("obesity-class3/severe obesity")
        else:print("make sure to enter only +ve values")
    except Exception as e:
        print(f'the error is {e}')
    n_of_t_user_input-=1
    


