#Exercise 1

#import os, time

#listOfEmail = ["Green","Eggs","And","Ham","Sam","I","Am"]
#listOfEmail = []

#def prettyPrint():
#  os.system("clear") # start by clearing the screen
#  print("listofEmail") # print the title of my program
#  print() # print a blank line
  
#  counter = 0
#  colourList = [91, 93, 92, 94, 95]
  
#  for email in listOfEmail: # use for loop to access list
#    colourCode = f"\033[{colourList[counter%len(colourList)]}m"
#    counter += 1
#    print(f"{colourCode}{counter}:{email}")
#  time.sleep(1)
#  print("\033[39m")
  
#while True:
#  print("SPAMMER Inc.")
#  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
#  if menu == "1":
#    email = input("Email > ")
#    listOfEmail.append(email)
#  elif menu =="2":
#    email = input ("Email > ")
#    if email in listOfEmail:
#      listOfEmail.remove(email)
#  elif menu == "3":
#    prettyPrint()  
#  time.sleep(1)
#  os.system("clear")

#Exercise 2
#import os, time
#listOfEmail = []
#def prettyPrint():
#  os.system("clear") 
#  print("listofEmail") 
#  print()
#  for index in range(len(listOfEmail)): # len counts how many items in a list
#    print(f"{index}: {listOfEmail[index]}") 
#  time.sleep(1)
#while True:
#  print("SPAMMER Inc.")
#  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
#  if menu == "1":
#    email = input("Email > ")
#    listOfEmail.append(email)
#  elif menu =="2":
#    email = input ("Email > ")
#    if email in listOfEmail:
#      listOfEmail.remove(email)
#  elif menu == "3":
#    prettyPrint() 
#  time.sleep(1)
#  os.system("clear")

#Fix my Code

#import os, time
#listOfFood = []

#def prettyPrint():
#  os.system("clear") 
#  print("listofFood") 
#  print()
#  counter = 1
#  for order in listOfFood: 
#    print(f"{counter}: {order}") 
#    counter += 1 
#  time.sleep(1)
  
#while True:
#  print("Yummy Food Restaurant")
#  menu = input("1. Order food\n2: Delete order\n3. Leave a review\n4. Delivery\n> ")
#  if menu == "1":
#    order = input("order > ")
#    listOfFood.append(order)
#  elif menu =="2":
#    order = input ("delete order> ")
#    if order in listOfFood:
#      listOfFood.remove(order)
#  elif menu == "4": 
#    prettyPrint() 
#    time.sleep(1)
#  os.system("clear")

# Day 34 Challenge
import os, time

listOfEmail = ["john@test.com","ben@test.com","mary@test.com","fran@test.com","julian@test.com","rob@test.com","sandra@test.com"]
#listOfEmail = []

def prettyPrint():
  os.system("clear") # start by clearing the screen
  print("listofEmail") # print the title of my program
  print() # print a blank line
  
  counter = 0
  colourList = [91, 93, 92, 94, 95]
  
  for email in listOfEmail: # use for loop to access list
    colourCode = f"\033[{colourList[counter%len(colourList)]}m"
    counter += 1
    print(f"{colourCode}{counter}:{email}")
  time.sleep(1)
  print("\033[39m", end="")

def startSpamming():
  print()
  for counter in range(min(len(listOfEmail),10)):
    os.system("clear")
    print(f"Dear {listOfEmail[counter]}\n\nIt has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.\n\nLove and hugs,\nIan Spammington III\n\n")
    time.sleep(0.7)
  input("Press enter to return to menu")
  
while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint()
  elif menu == "4":
    startSpamming()
  time.sleep(1)
  os.system("clear")