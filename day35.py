# Day 35 Challenge

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
  menu = input("Do you want to view, add, edit or remove an item from your to do list?\n")
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
      confirm = input("Are you sure? ")
      if confirm.lower() == "yes":
        toDoList.remove(item)
        time.sleep(0.2)
    else:
      print(f"\n{item} not in list!")      
  elif menu.lower() == "edit":
    os.system("clear")
    alter = input("Which item would you like to edit? ")
    match = 0
    counter=0
    for item in toDoList:
      if item == alter:
        match = 1
        toDoList[counter] = input("")
      counter += 1
    if match == 0:
      print(f"Item '{alter}' not found.")
      time.sleep(0.7)
  elif menu.lower() == "exit":
    break
  