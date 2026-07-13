#nlwh rpbh sywk gebc



import smtplib
import ssl
from email.message import EmailMessage
Sender="knsknsk10@gmail.com"
passkey="nlwh rpbh sywk gebc"
receiver="knsknsk10@gmail.com"
message=EmailMessage()
message["from"]=Sender
message["to"]=receiver
message["subject"]="namaskaram"
message.set_content(f'''"bayataki
pora
chovitina
kodaka"''')
context=ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com",port=587)as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login(Sender,passkey)
    smtp.send_message(message)
    smtp.quit()
    
