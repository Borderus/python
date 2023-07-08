#Exercise 1

#f = open("savedFile.txt", "w")

#f.write("Hello there\n\nGeneral Kenobi")
#f.close()

#Exercise 2
#f = open("savedFile.txt","w")
#while True:
#  whatText = input("> ")
#  if whatText.lower().strip() == "quit":
#    break
#  f.write(f"{whatText}\n")
#  f.close()
#  f = open("savedFile.txt", "a+")
#f.close()

#Exercise 3
#f = open("savedFile.txt", "a+")
#whatText = input("> ")
#f.write(f"{whatText}\n")
#whatText = input("> ")
#f.write(f"{whatText}\n")
#f.close()

#Fix my Code
#f = open("savedFoal.txt", "a+")
#whatText = input("> ")
#f.write(f"{whatText}\n")
#whatText = input("> ")
#f.write(f"{whatText}\n")
#f.close

#Day 48 Challenge
#Initialise
import os, time
#Create file
if not os.path.exists("highscores.txt"):
  print("Creating file...\n")
  f = open("highscores.txt", "w")
  f.write("User    Score\n")
  f.close()
  time.sleep(0.7)
  os.system("clear")

print("🌟HIGH SCORE TABLE🌟")

while True:
  initials = input("\nInput your initials > ").upper()[0:4]
  score = max(min(int(input("Input your score > ")),999999),0)

  #Add to table
  f = open("highscores.txt", "a+")
  f.write(f"{initials:<4}{score:>9}\n")
  f.close()

  print("\nAdded to table")
  loopCheck = input("Add another? ")
  if loopCheck.lower().strip()[0] == "n":
    break