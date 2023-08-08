from replit import db
import hashlib, time, os, datetime

#---------------------GET OR CREATE PW------------------------
def getPW():
  try:
    f = open("pw.txt", "r")
    truePW = f.readline()
    f.close()
  except FileNotFoundError:
    f = open("pw.txt", "w")
    hashGen = hashlib.sha512()
    hashGen.update(input("Create a password: ").encode("utf-8"))
    hash = hashGen.hexdigest()
    f.write(hash)
    f.close()
    print("Password created successfully.")
    getPW()
  return truePW

#----------------------PW CHECK USER--------------------------
def checkPW():
  truePW = getPW()
  hashGen = hashlib.sha512()
  hashGen.update(input("Enter password: ").encode("utf-8"))
  success = truePW == hashGen.hexdigest()
  return success
  
#------------------------GET KEYS-----------------------------
def getKeys():
  entryList = []
  keys = db.keys()
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
login = checkPW()
if login:
  print("\nLog-in successful")
  time.sleep(0.7)
  os.system("clear")
  while True:
    entryList = getKeys()
    menu = printMenu()
    if menu == "a":
      addItem()
    elif menu == "v":
      viewItems(entryList)
    elif menu == "q":
      break
    os.system("clear")
if not login:
  print("\nLog-in failed")
  time.sleep(0.7)
  os.system("clear")