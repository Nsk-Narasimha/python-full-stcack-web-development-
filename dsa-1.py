email='saketha@codegnan.com'
print(email[8:16])
email_id=['knsknsk10@gmail.com','narasimha@gmail.com','sai_kumar546@yahoo.com','info@codegnan.com']
print(len(email_id))
print(*email_id[-1:-3:-1])
email_id.extend(['abc@gmail.com','xyz@gmail.com'])
print(email_id)
for mail in email_id:
    print(f'the person is {mail}')
users={}
print(type(users))
for i in range(len(email_id)):
    users[i+1]=email_id[i]

print(dict(enumerate(email_id,1)))

#users=dict.(email_id)


