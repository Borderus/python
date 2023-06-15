#A rock paper scissors game

playerOneScore = 0
playerTwoScore = 0

print("Please use R, P or S")

from getpass import getpass as input
while True:

  playerOne = input("Player 1: ")
  playerTwo = input("Player 2: ")

  if playerOne.upper() == "R":
    if playerTwo.upper() == "R":
      outcome = "Tie!"
    elif playerTwo.upper() == "P":
      outcome = "Player 2 wins this round!"
      playerTwoScore += 1
    elif playerTwo.upper() == "S":
      outcome = "Player 1 wins this round!"
      playerOneScore += 1
    else:
      outcome = "ERROR: PLAYER 2 INVALID INPUT"
  elif playerOne.upper() == "P":
    if playerTwo.upper() == "R":
      outcome = "Player 1 wins this round!"
      playerOneScore += 1
    elif playerTwo.upper() == "P":
      outcome = "Tie!"
    elif playerTwo.upper() == "S":
      outcome = "Player 2 wins this round!"
      playerTwoScore += 1
    else:
      outcome = "ERROR: PLAYER 2 INVALID INPUT"
  elif playerOne.upper() == "S":
    if playerTwo.upper() == "R":
      outcome = "Player 2 wins this round!"
      playerTwoScore += 1
    elif playerTwo.upper() == "P":
      outcome = "Player 1 wins this round!"
      playerOneScore += 1
    elif playerTwo.upper() == "S":
      outcome = "Tie!"
    else:
      outcome = "ERROR: PLAYER 2 INVALID INPUT"
  else: 
    outcome = "ERROR: PLAYER 1 INVALID INPUT"

  print("")
  print(outcome)
  print("")
  print("Score: Player One "+str(playerOneScore)+" - "+str(playerTwoScore)+" Player Two")
  print("")

  if playerOneScore >= 3:
    print("Player 1 wins the game!")
    break
  if playerTwoScore >= 3:
    print("Player Two wins the game!")
    break