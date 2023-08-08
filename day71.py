# Exercise 1 - Hashing
#from replit import db

#userName = "Ben"
#password = "guest"
#password = hash(password)
#db[userName] = password

#print(db["Ben"])

#Exercise 2 - Login for a hashed password
#from replit import db

#userName = input("Username: ")
#password = hash(input("Password: "))

#login = False
#for user, pw in db.items():
#  if userName == user and pw == password:
#    login = True
#    print("Login successful.")
#if login == False:
#  print("Login failed: Username and/or password not found.")

#Exercise 3 - Salting
# People keep databases of known hashes in order to get around the trapdoor difficulty
# We can give these folks some trouble by salting - adding a random value onto the password to change the hash

#from replit import db

#password = "baldy1"
#salt = 10221
#newPassword = hash(f"{password}{salt}")
#db["David"] = {"password":newPassword, "salt":salt}

#password = "baldy2"
#salt = 39820
#newPassword = hash(f"{password}{salt}")
#db["Roger"] = {"password":newPassword, "salt":salt}

#userName = input("Username: ")
#try:
#  password = hash(f'{input("Password: ")}{db[userName]["salt"]}')
#  login = False
#  for user, pw in db.items():
#    if userName == user and pw == password:
#      login = True
#      print("Login successful.")
#  if login == False:
#    print("Login failed: Username and/or password not found.")
#except KeyError:
#    print("Login failed: Username and/or password not found.")

#Fix my code

#from replit import db

#ans = input("Password > ") 
#salt = db["David"]["salt"] 
#newPassword = f"{ans}{salt}"
#newPassword = hash(newPassword) 

#if newPassword == db["David"]["password"]: 
#  print("Login successful")

#-------------------Day 71 Challenge-------------------

from replit import db
import random, os, time

# ----------------------Add user-----------------------
def createUser():
    os.system("clear")
    time.sleep(0.5)
    userName = input("Username: ")
    time.sleep(0.7)
    password = input("Password: ")
    salt = random.randint(10000,99999)
    newPassword = hash(f"{password}{salt}")
    
    db[userName] = {"password":newPassword, "salt":salt}
    time.sleep(0.7)
    print("\nDetails stored.")
    time.sleep(1.2)

# ------------------------Login------------------------
def login():
    os.system("clear")
    time.sleep(0.5)
    reqUser = input("Username: ")
    time.sleep(0.7)
    reqPW = input("Password: ")

    login = False
    for user in db.keys():
      if user == reqUser and db[user]["password"] == hash(f"{reqPW}{db[user]['salt']}"):
        login = True
    return login
    time.sleep(1.2)

# ----------------------Main loop----------------------

while True:
  os.system("clear")
  time.sleep(0.5)
  print("Login System")
  time.sleep(0.7)
  print()
  menu = input("1: Add User, 2: Login > ")

  if menu == "1":
    createUser()
  elif menu == "2":
    login=login()
    
    if login == False:
      time.sleep(0.7)
      print("\nLogin failed: Username and/or password not found.")
    else:
      time.sleep(0.7)
      print("\nLogin successful.")
      break
  elif menu == "q":
    break