# Python Bingo
import math, random, os, time

playerList = ["Ben", "Keith", "Steve", "Roger", "Danny", "Amos", "Jack"]
players = {}

for player in playerList:
  players[player] = {"uncalled": [], "called": []}

#METHOD TO TAKE FROM ONE LIST AND ADD TO ANOTHER
def moveBall(addlist, takelist, item):
  if item in takelist:
    takelist.remove(item)
    addlist.append(item)

#------------SET UP CAGE---------------
def fillCage():
  bingoCage = []
  for counter in range(1,91):
    bingoCage.append(counter)
  return bingoCage

#----------POPULATE TICKETS------------
#Get number of batches to cycle through
batchCount = math.ceil(len(players)/6)

#For each batches, take 6 players and partition numbers
for counter in range(batchCount):
  batchNumberPool = fillCage()
  batchPlayers = playerList[6*counter: 6*counter+6]
  #Cycle through players
  for counter2 in range(min(6, len(batchPlayers))):
    #Cycle through decades
    for counter3 in range(9):
      startpos = 10*counter3
      endpos = (counter3+1)*10
      #Get random position on sheet
      loop=True
      while loop:
        newPos = random.randint(0, len(batchNumberPool)-1)
        if (batchNumberPool[newPos] > startpos) and (batchNumberPool[newPos] <= endpos):
          loop = False
      #Get value
      newNum = batchNumberPool[newPos]
      #Move value into ticket
      moveBall(players[batchPlayers[counter2]]["uncalled"], batchNumberPool, newNum)

    #Assign the rest of the numbers randomly
  for counter in range(6):
    for counter2 in range(min(6, len(batchPlayers))):
      newPos = random.randint(0, len(batchNumberPool)-1)
      newNum = batchNumberPool[newPos]
      moveBall(players[batchPlayers[counter2]]["uncalled"], batchNumberPool, newNum)

#Number of tickets to create is ceiling number of players divided by 6
#For each batch of 6 tickets, partition the 90 numbers in the ticket pool amongst them
#Do this by:
#Assigning each ticket a number in each 10 numbers from the ticket pool (i.e. 1-10, 11-20, 21-30, ...) and removing the number from the ticket pool
#Then looping through the tickets and assigning the numbers to them, removing those from the pool.


#-------------PLAY GAME----------------
cage=fillCage()
usedBalls = []
while True:
  breakFlag = False
  os.system("clear")
  randpos = random.randint(0, len(cage)-1)
  randnum = cage[randpos]
  print(f"The number drawn is: {randnum}")
  moveBall(usedBalls, cage, randnum)

  for player, playerlist in players.items():
    moveBall(playerlist["called"], playerlist["uncalled"], randnum)
    print(player)
    print(playerlist["uncalled"])
    if playerlist["uncalled"] == []:
      print(f"\n{player} wins!")
      breakFlag = True
      break

  playerentry = input()
  if playerentry == "q":
    breakFlag = True

  if breakFlag == True:
    break

#Could add row logic

#-------------GET CARD-----------------

#TODO

#------------EMAIL PLAYERS-------------

#TODO