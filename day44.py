#Exercise 1

#def prettyPrint(listOfShame):
#  print() 
#  for row in listOfShame: 
#    for item in row: 
#     print(f"{item:^10}", end=" | ")  
#    print() 
#  print()

#listOfShame = []

#while True:
#  name = input("What is your name? ")
#  age = input("What is your age? ")
#  pref = input("What is your computer platform? ")

#  row = [name, age, pref]
#  listOfShame.append(row)
  
#  exit = input("Exit? y/n ")
#  if (exit.strip().lower()[0] == "y"):
#    break

#  prettyPrint(listOfShame)

#Exercise 1

#def prettyPrint(listOfShame):
#  print() 
#  for row in listOfShame: 
#    for item in row: 
#     print(f"{item:^10}", end=" | ")  
#    print() 
#  print()

#listOfShame = []

#while True:
#  menu = input("Add or remove? ")

#  if (menu.strip().lower()[0] == "a"):
#    name = input("What is your name? ")
#    age = input("What is your age? ")
#    pref = input("What is your computer platform? ")

#    row = [name, age, pref]
#    listOfShame.append(row)

#  if (menu.strip().lower()[0] == "r"):
#    searchName = input("Who would you like to remove from the list? ")
#    for row in listOfShame:
#      if searchName == row[0]:
#        listOfShame.remove(row)
    
#  print()
#  prettyPrint(listOfShame)
  
#  exit = input("Exit? y/n ")
#  if (exit.strip().lower()[0] == "y"):
#    break

#Fix My Code

#listOfShame = [] 
#while True: 
#  menu = input("Add or Remove?") 
#  if(menu.strip().lower()[0]=="a"): 
    
#    name = input("What is your name? ")
#    age = input("What is your age? ")
#    pref = input("What is your computer platform? ")
    
#    row = [name, age, pref] 
  
#    listOfShame.append(row) 
    
#  else: 
#    name = input("What is the name of the record to delete?") 
#    for row in listOfShame:
#      if name in row: 
#        listOfShame.remove(row) # remove the whole row if name is in it
#  print(listOfShame)

# Day 44 Challenge

#2D Lists
#Exercise 1

#my2DList = [["Johnny", 21, "Mac"],
#            ["Sian", 19, "PC"],
#            ["Gethin", 17, "PC"]]

#print(my2DList)
#print()
#print(my2DList[2])
#print()
#print(my2DList[2][0])

#Exercise 2

#print()

#my2DList[1][2] = "Linux"
#print(my2DList[1])

#Fix My Code

#my2DList =  [["Johnny", 21, "Mac"],
#            ["Sian", 19, "PC"],
#            ["Gethin", 17, "PC"] ]
#print(my2DList[0][1])

import random, os, time

bingoNos = []
bingoCard = []

while len(bingoNos) < 9:
  number = random.randint(0,90)
  if number not in bingoNos:
    bingoNos.append(number)

bingoNos.sort()

for counter1 in range(3):
  temp = []
  for counter2 in range(3):
    if counter1 != 1 or counter2 != 1:
      temp.append(str(bingoNos[3*counter1 + counter2]))
    else:
      temp.append("BINGO")
  bingoCard.append(temp)

calledNumbers = 0

for counter in range(15):
  os.system("clear")
  print("\033[4;93mDavid's Nan's Bingo Card Generator")
  print()
  for counter1 in range(3):
    for counter2 in range(3):
      print(f"{bingoCard[counter1][counter2]:^5}", end="")
      if counter2 != 2:
        print(" | ", end="")
    print()
  print()
  nextNo = input("\033[24;39mNext Number: ")
  for row in bingoCard:
    for entry in row:
      if entry.strip() == nextNo.strip() and nextNo.strip() != "BINGO":
        bingoCard[bingoCard.index(row)][row.index(entry)] = "X"
        calledNumbers += 1
  if calledNumbers == 8:
    print("You win!")
    break
  print(calledNumbers)
  time.sleep(0.8)