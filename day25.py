#Exercise #1

#subroutine has parameter called `number`
#`number` shows how many numbers we want the pin to have
#def pinPicker(number):
#  import random
#  pin = "" #this is the empty string
#  for i in range(number): #for loop shows defined amount of random numbers
#    pin += str(random.randint(0,9)) #we want a string of random numbers between 0-9
#  return pin

#myPin = pinPicker(4) #4 means we want 4 random numbers
#print(myPin)

# Fix My Code

#def area_square(side1, side2):
#  area_square = side1 * side2
#  return area_square
#area = area_square(4, 12)
#print(area)

#Day 25 Challenge


import random
  
def infinityDice(sides):

  outcome = random.randint(1,sides+1)
  return outcome

def charHealth():
  healthPoints = infinityDice(6) * infinityDice(8)
  return healthPoints

print("Character stats generator")

while True:
  charName = input("Name your warrior: ")
  if charName == "exit":
    break
  print("Their health is "+str(charHealth())+"hp\n")