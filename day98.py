#----------------------------------DAY 94 CHALLENGE---------------------------------------------
#In order to run this, an app password needs to be set up on Gmail and the username and password
#added into the Repl as a secret.

import schedule, time, os, smtplib, random
from email.message import EmailMessage

username = os.environ['mailUsername']
password = os.environ['mailPassword']

#------------GET JOKES---------------

jokes = []
f = open("jokes.txt", "r")
for line in f:
  processLine = f.readline().replace('\n','')
  if processLine != '':
    jokes.append(processLine)
f.close()

#-----------GENERATE JOKE------------

def getJoke():
  randint = random.randint(0,len(jokes)-1)
  randjoke = jokes[randint]
  return randjoke

#------------SEND EMAIL--------------

def sendMail():
  msg = EmailMessage()
  msg['Subject'] = 'Hello'
  msg['To'] = 'benback96@gmail.com'
  msg['From'] = 'benback96@gmail.com'
  email = getJoke()
  msg.set_content(email)
  server = "smtp.gmail.com"
  port=587
  s = smtplib.SMTP(host = server, port=port)
  s.starttls()
  s.login(username, password)

  s.send_message(msg)
  del msg

sendMail()

schedule.every(1).minutes.do(lambda: sendMail())

while True:
  schedule.run_pending()