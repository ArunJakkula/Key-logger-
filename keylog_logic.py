#This adds all the extra funtionalities that I proposed 

import smtplib
import ssl
from email.message import EmailMessage
import rsa
import time
publicKey, privateKey = rsa.newkeys(512)
word_list = ["arun","shine","hemanth","yerri"]
def startmail():

    email_sender = 'arunjakkula2044@gmail.com'
    email_password = 'mmyg dsxm gueo obrf'
    email_receiver = 'arunjakkula2044@gmail.com'
    subject = 'The code has been started '
    body = "here goes your private key  :  /n" + str(privateKey)

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

def read():

    with open("log.txt", 'a') as f:
        f.write(" end")

    with open('log.txt', 'r') as file:
            # reading each line
            for line in file:

                # reading each word
                for word in line.split():
                   b = word + " "
                   if word == "end":
                       with open("log.txt", 'w') as file:
                           file.write("")
                   else:
                       for a in word_list:
                           if word == a:
                               sendmail()

                   encMessage = rsa.encrypt(b.encode(),publicKey)
                   with open("log1.txt", "a") as file:
                        file.write(str(encMessage))

def sendmail():
    email_sender = 'arunjakkula2044@gmail.com'
    email_password = 'mmyg dsxm gueo obrf'
    email_receiver = 'arunjakkula2044@gmail.com'
    subject = 'Alert'
    body = "An illegal word has been found"
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())



startmail()
while True:
    read()
    time.sleep(30)
