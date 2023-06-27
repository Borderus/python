# Exercise 1

#name = input("What's your name? ")
#if name.lower().strip() =="david":
#  print("Hello Baldy!")
#else: 
#  print("What a beautiful head of hair!")

#Can also use .upper(), .title() (capitalise each word), .capitalise() (capitlise sentence)

#Exercise 2

#myList = []

#def printList():
#  print()
#  for i in myList:
#    print(i)
#  print()

#while True:
#  addItem = input("Item > ").strip().capitalize()
#  if addItem not in myList:
#    myList.append(addItem) 
#  printList()

#Fix My Code

#whatToEat = input("What do you fancy for dinner? ")

#if whatToEat.lower().strip() == "pasta": 
#  print("Get out the pasta maker.")
#elif whatToEat.lower().strip() == "tacos":
#  print("Let's do Taco Tuesday!")
#else: 
#  print("Go search the fridge.")

#Day 36 Challenge

import time, os, sys

listOfNames = []

def printList(list):
  for item in list:
    print(item)

def breakCheck(var):
  if var.lower().strip() == "exit":
    sys.exit()

def getNames(list):
  forename = input("What is the person's first name? ").strip().title()
  breakCheck(forename)
  time.sleep(0.2)
  surname = input("And what is the person's surname? ").strip().title()
  breakCheck(surname)  
  time.sleep(0.2)
  name = f"{forename} {surname}".strip()
  if name not in listOfNames:
    listOfNames.append(name)

while True:
  os.system("clear")
  getNames(listOfNames)
  print()
  printList(listOfNames)
  time.sleep(0.7)