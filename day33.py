#Exercise 1
#def printList(list):
#  print()
#  for item in list:
#    print(item)
#  print()    
#
#myAgenda = []
#
#while True:
#  item = input("What's next on the agenda? ")
#  
#  if item == "exit":
#    break
#    
#  myAgenda.append(item)
#  printList(myAgenda)

#Exercise 2
#def printList(list):
#  print()
#  for item in list:
#    print(item)
#  print()    

#myAgenda = []

#while True:
#  menu = input("Add or remove? ")
#  if menu.lower() == "add":
#    item = input("What's next on the agenda? ")
#    myAgenda.append(item)
#    printList(myAgenda)
#  elif menu.lower() == "remove":
#    item = input("What do you want to remove? ")
#    myAgenda.remove(item)
#    printList(myAgenda)
#  elif menu == "exit":
 #   break

#Fix My Code

#def printList():
#  print() 
#  for item in myPartyList:
#    print(item)
#  print() 

#myPartyList = []

#while True:
#  menu = input("add or remove?: ")
#  if menu == "add":
#    item = input("Who should I add to the party list?: ")
#    myPartyList.append(item)
#  elif menu == "remove":
#    item = input("Who should I remove from the party list?: ")
#    if item in myPartyList:
#      myPartyList.remove(item)
#    else:
#      print(f"{item} was not in the list")
#  printList()

# Day 33 Challenge

import os, time

def printList(list):
  print() 
  for item in list:
    print(item)
  print()

toDoList=[]

title = "To Do List Manager:"
title2 = "To Do List"
print(f"{title:^49}")

while True:
  os.system("clear")
  print(f"{title:^49}")  
  menu = input("Do you want to view, add or edit your to do list?\n")
  if menu.lower() == "view":
    os.system("clear")
    print(f"{title2:^49}")
    printList(toDoList)
    input("Press enter to return to menu")
  elif menu.lower() == "add":
    time.sleep(0.2)
    item = input("\nWhat would you like to add? ")
    toDoList.append(item)
    time.sleep(0.2)
  elif menu.lower() == "remove":
    time.sleep(0.2)
    item = input("\nWhat have you completed? ")
    if item in toDoList:
      toDoList.remove(item)
      time.sleep(0.2)
    else:
      print(f"\n{item} not in list!")
      time.sleep(0.7)
  elif menu.lower() == "exit":
    break
  