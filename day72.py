from replit import db
import time, os, datetime, random

#------------------------LOGIN MENU---------------------------
def loginMenu():
  time.sleep(0.5)
  print("Log-in menu\n")
  if "login" in db:
    time.sleep(0.7)
    username = input("Enter username: ")
    time.sleep(0.5)
    password = input("Enter password: ")
    if username == db["login"]["username"] and hash(password+db["login"]["salt"]) == db["login"]["password"]:
      print("\nLogin successful.")
      time.sleep(0.7)
      return True
    else:
      print("\nLogin failed. Username and/or password not found...")
      time.sleep(1.2)
      os.system("clear")
  else:
    time.sleep(0.7)
    username = input("Enter username: ")
    time.sleep(0.5)
    password = input("Enter password: ")
    salt = str(random.randint(10000,99999))
    fullPW = hash(password+salt)
    db["login"] = {"username": username, "password": fullPW, "salt": salt}
  
#------------------------GET KEYS-----------------------------
def getKeys():
  entryList = []
  keys = db.keys()
  keys.remove("login")
  for key in keys:
    entryList.append(key)
  entryList.sort(reverse=True)
  return entryList

#-----------------------PRINT MENU----------------------------
def printMenu():
  print(f"{'SUPER SECRET DIARY':^40}")
  print()
  print()
  return input("Add entry or view? ").strip().lower()[0]

#------------------------ADD ITEM-----------------------------
def addItem():
  timestamp = datetime.datetime.now()
  entry = input("> ")
  db[timestamp] = {"entry": entry}
  entryList.append(entry)
  
#-----------------------VIEW ITEMS----------------------------
def viewItems(entryList):
  for entry in entryList:
    print(f"{str(entry)[0:16]:<40}")
    print(f"{db[entry]['entry']:>40}\n")
    menu = input("Return to menu or view another? ").strip().lower()[0]
    if menu == "y":
      return
    print()
  input("\nNo more entries - press enter to return to menu...")
  
#------------------------RUN CODE-----------------------------
login = loginMenu()
if login:
  os.system("clear")
  while True:
    entryList = getKeys()
    menu = printMenu()
    if menu == "a":
      addItem()
    elif menu == "v":
      viewItems(entryList)
    elif menu == "q":
      os.system("clear")
      break
    os.system("clear")