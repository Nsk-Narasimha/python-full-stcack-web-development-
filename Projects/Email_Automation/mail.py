"""import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
#print(server) start the connection
server.starttls()
#login
server.login("knsknsk10@gmail.com","khjp fjlo rehh iyts")
msg="sanjay anna big fan anna "
server.sendmail("knsknsk10@gmail.com",["sanjay43650@gmail.com","knsknsk10@gmail.com"],msg)
server.quit()
print("mail sent")"""'''
#otp
import math,random,smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
#otp=random.randint(0000,9999)
server.login("knsknsk10@gmail.com","khjp fjlo rehh iyts")
msg=f"sanjay anna big fan anna {otp}"
server.sendmail("knsknsk10@gmail.com",["sanjay43650@gmail.com","knsknsk10@gmail.com"],msg)
server.quit()
print("mail sent")
if(otp==int(input("enter sajay fan validation code:"))):
    print("you are true fan")
else:
    print("you not a fan at all")

import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
From="knsknsk10@gmail.com"
to="knsknsk10@gmail.com"
subject="python full stack"
msg=MIMEMultipart()
msg['From']=From
msg['To']=to
msg['Subject']=subject
text="hi guys"
msg['body']=text
msg.attach(MIMEText(msg['body'],'plain'))
text=msg.as_string()
print(type(msg))
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("knsknsk10@gmail.com","khjp fjlo rehh iyts")
server.sendmail(From,to,text)
#print(help(print))
server.quit()
print("mail sent")
'''
import email,os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
From="knsknsk10@gmail.com"
to="sanjay43650@gmail.com"
subject="python full stack"
body="we have understood how to send automated emails using python"
attach="..\..\myqr.png"
msg=MIMEMultipart()
msg['From']=From
msg['To']=to
msg['Subject']=subject
msg.attach(MIMEText(body))
part=MIMEBase('application','octet-stream')
print(part)
part.set_payload(open(attach,"rb").read())
encoders.encode_base64(part)
part.add_header('content-Disposition',f'attachment;filename={os.path.basename(attach)}')
msg.attach(part)
text=msg.as_string()
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("knsknsk10@gmail.com","khjp fjlo rehh iyts")
server.sendmail(From,to,text)
server.quit()
print("mail sent")
