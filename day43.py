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

import random

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
      temp.append(bingoNos[3*counter1 + counter2])
    else:
      temp.append("BINGO")
  bingoCard.append(temp)

print("\033[4;93mDavid's Nan's Bingo Card Generator")
print()
for counter1 in range(3):
  for counter2 in range(3):
    print(f"{bingoCard[counter1][counter2]:^5}", end="")
    if counter2 != 2:
      print(" | ", end="")
  print()
print("\033[4;39m")