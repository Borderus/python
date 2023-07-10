#Exercise 1

#myEvents = []

#f = open("calendar.txt", "r")
#myEvents = eval(f.read())
#f.close()

#def prettyPrint():
#  print()
#  for row in myEvents:
#    print(f"{row[0]:^15}{row[1]:^15}")

#while True:
#  menu = input("1: Add\n2: Remove\n")

#  if menu == "1":
#    event = input("What event? ").capitalize()
#    date = input("What date? ")
#    row = [event, date]
#    myEvents.append(row)
#    prettyPrint

#  elif menu == "2":
#    criteria = input("What event do you want to remove?").title()
#    for row in myEvents:
#      if criteria in row:
#        myEvents.remove(row)

#  f = open("calendar.txt", "w")
#  f.write(str(myEvents))
#  f.close()

#Fix My Code

#myEvents = []

#f = open("calendar.txt","r")
#myEvents = eval(f.read())
#f.close()

#def prettyPrint():
#  print()
#  for row in myEvents:
#    print(f"{row[0] :^15} {row[1] :^15}")
#  print()
  
#while True:
#  menu = input("1: Add, 2: Remove\n")
  
#  if menu == "1":
#    event = input("What event?: ").capitalize()
#    date = input("What date?: ")
#    row = [event,date]
#    myEvents.append(row)
#    prettyPrint()
    
#  else:
#    criteria = input("What event do you want to remove?: ").title()
#    for row in myEvents:
#      if criteria in row:
#        myEvents.remove(row)


#f = open("calendar.txt", "w") 
#f.write(str(myEvents)) 
#f.close()

# Day 51 Challenge

#-------------------------------- IMPORT -------------------------------
import os, time

#-------------------------------- ASSIGN -------------------------------
toDoList = []

#-------------------------- ADDITEM SUBROUTINE -------------------------
def addItem():
  print()
  temp.append(input("What is the task? > "))
  temp.append(input("When is it due by? > "))
  temp.append(input("What is the priority? > ").upper())

  toDoList.append(temp)
  print("\nThanks, this task has been added.")

#-------------------------- VIEWITEM SUBROUTINE ------------------------
def viewList():
  viewMenu = input("Would you like to view all, or a particular priority? (high/med/low) > ")
  print()
  for item in toDoList:
    if ((viewMenu.lower().strip()[0] == "a") or (viewMenu.upper().strip()[0] == item[2][0])):
      print(f"> {item[0]}: Due {item[1]}, priority {item[2]}.")

#-------------------------- EDITITEM SUBROUTINE ------------------------
def editItem():
  changeItem = input("Which item would you like to change? > ")
  itemNotFound = 1
  for item in toDoList:
    if item[0].lower().strip() == changeItem.lower().strip():
      itemIndex = toDoList.index(item)
      itemNotFound = 0

      print(f"Task: {toDoList[itemIndex][0]}")
      temp.append(input("What is the task? > "))
      print(f"Due date: {toDoList[itemIndex][1]}")
      temp.append(input("When is it due by? > "))
      print(f"Priority: {toDoList[itemIndex][2]}")
      temp.append(input("What is the priority? > ").upper())

      toDoList[itemIndex] = temp
  if itemNotFound:
    print("Item not found.")

#-------------------------- REMITEM SUBROUTINE -------------------------
def remItem():
  changeItem = input("Which item would you like to remove? > ")
  itemNotFound = 1
  for item in toDoList:
    if item[0].lower().strip() == changeItem.lower().strip():
      toDoList.remove(item)
      itemNotFound = 0
      print("Item removed successfully.")
  if itemNotFound:
    print("Item not found.")

#------------------------------ RUN LIST -------------------------------

#Autoload
filename = "ToDoList.txt"
if os.path.exists(filename):
  f = open(filename, "r")
  toDoList = eval(f.read())
  f.close()

while True:
  os.system("clear")
  temp = []
  
  print("To Do List")
  print()
  menu = input("Do you want to add, view, edit or remove an item? > ")

  if menu.lower().strip()[0] == "a":
    addItem()
  elif menu.lower().strip()[0] == "v":
    viewList()
  elif menu.lower().strip()[0] == "e":
    editItem()
  elif menu.lower().strip()[0] == "r":
    remItem()

  time.sleep(1)

  f = open(filename, "w")
  f.write(str(toDoList))
  f.close()
  
  repeatMenu = input("Do you want to see the menu again or quit? > ")
  if repeatMenu.lower().strip()[0] == "q":
    break