# Day 53 Challenge
import os, time
filename = "inventory.txt"

#-----------------LOAD RECORDS--------------------
def autoLoad(filename):
  try:
    f = open(filename, "r")
    inventory = f.read().split("\n")
    try:
      inventory.remove("")
    except ValueError:
      time.sleep(0)
    f.close()
  except FileNotFoundError:
    print("File not found - starting a new inventory.\n")
    inventory = []
    time.sleep(1)
    os.system("clear")
  return inventory

#----------------SAVE RECORDS--------------------
def autoSave(filename, inventory):
  f = open(filename, "w")
  for item in inventory:
    f.write("\n")
    f.write(item)
  f.close()

#----------------ADD RECORDS---------------------
def addItem():
  print(">")
  time.sleep(0.5)
  item = input("> What would you like to add?\n> ").strip().title()
  inventory.append(item)
  time.sleep(0.5)
  print(">")
  time.sleep(0.5)
  print(f"> {item} successfully added!")
  time.sleep(1)

#---------------REMOVE RECORDS-------------------
def removeItem():
  try:
    print(">")
    time.sleep(0.5)
    item = input("> What would you like to remove?\n> ").strip().title()
    inventory.remove(item)
  except ValueError:
    print("Item not found")
  time.sleep(0.5)
  print(">")
  time.sleep(0.5)
  print(f"> {item} successfully removed!")
  time.sleep(1)
  
#----------------VIEW RECORDS--------------------
def viewItem():
  time.sleep(0.5)
  print(">")
  time.sleep(0.5)
  item = input("> Which item would you like to view?\n> ").strip().title()
  time.sleep(0.5)
  print(">")
  time.sleep(0.5)
  print(f"> You have {inventory.count(item)} {item}.")
  time.sleep(1)

#------------------RUN CODE----------------------
while True:
  inventory = autoLoad(filename)

  print(f"{'Inventory':^45}")
  menu = input("\n1: Add  2: Remove  3: View  4: Quit\n> ")

  if menu.lower().strip()[0] == "1" or menu.lower().strip()[0] == "a":
    addItem()
  elif menu.lower().strip()[0] == "2" or menu.lower().strip()[0] == "r":
    removeItem()
  elif menu.lower().strip()[0] == "3" or menu.lower().strip()[0] == "v":
    viewItem()
  elif menu.lower().strip()[0] == "4" or menu.lower().strip()[0] == "q":
    break

  autoSave(filename, inventory)
  os.system("clear")