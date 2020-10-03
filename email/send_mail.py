#simple mail transfer protocal library
import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template
email = EmailMessage()
def getValues(fromP,toP,subP,messP):
   global email
   #email properties
   email['from'] = str(fromP)
   email['to'] = str(toP)
   email['subject'] = str(subP)
   email.set_content(str(messP))
   #sends email
   with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
      smtp.ehlo()
      smtp.starttls()
      #sender's email address and email password would go here
      smtp.login('email', 'password')
      smtp.send_message(email)
   print('email is sent')
# def getValues(a,b,c):
#    print(a,b,c)