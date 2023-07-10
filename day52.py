# Exercise 1 - Exceptions

#myStuff = []

#try:
#  f=open("Stuff.mine", "r")
#  myStuff = eval(f.read())
#  f.close
#except Exception as err:
#  print("ERROR: File not found...")
#  print(err)

#for row in myStuff:
#  print(row)

#Exercise 2 - Specific Exceptions
# https://www.w3schools.com/python/python_ref_exceptions.asp
#try:
#  test = 1/0
#except ZeroDivisionError as err:
#  print(err)

#Exercise 3 - Traceback

#debugMode = True
#myStuff = []

#try:
#  f=open("Stuff.mine", "r")
#  myStuff = eval(f.read())
#  f.close
#except Exception:
#  if debugMode:
#    print(traceback)

#for row in myStuff:
#  print(row)

#Fix my code

#myStuff = []

#try:  
#  f = open("Stuff.mine","r")
#  myStuff = eval(f.read())
#  f.close()
#except:
#  print(traceback)

#for row in myStuff:
#  print(row)

# Day 52 Challenge
import os, time
filename = "pizzaorder.txt"
orderList = []
#-----------------LOAD RECORDS--------------------
try:
  f = open(filename, "r")
  while True:
    order = f.readline().split()
    if order == []:
      break
    orderList.append(order)
    print(orderList)
  f.close()
except FileNotFoundError:
  print("File not found - starting a new list.\n")
  time.sleep(1)
  os.system("clear")

#----------------GET USER INPUT-------------------
loopInd = True

while loopInd == True:
  loopInd = False
  try:
    quantity = int(input("How many pizzas? "))
  except ValueError:
    loopInd = True
    print("\nInvalid input - please enter a numeric character.\n")

loopInd = True

while loopInd == True:
  loopInd = False
  try:
    size = int(input("What size? "))
  except ValueError:
    loopInd = True
    print("\nInvalid input - please enter a numeric character.\n")

name = input("What is your name? ")
price = str(quantity*size)

print(f"Thanks {name}, your pizza will cost {price}.")

orderList.append([name, price])

#----------------SAVE RECORDS--------------------
firstobs = True
f = open(filename, "w")
for order in orderList:
  if firstobs:
    firstobs = False
  else:
    f.write("\n")
  f.write(order[0]+" "+order[1])
f.close()