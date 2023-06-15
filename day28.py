#Day 28 Challenge

import random, os, time

#Have user input name
def name():
  name = input("Enter the character name: ")
  return name

#Randomly generate species
def species():
  speciesArray = ["Dwarf", "Elf", "Gnome", "Halfling", "Human", "Centaur", "Goblin", "Hobgoblin", "Orc"]
  species = speciesArray[random.randint(0,len(speciesArray)-1)]
  return species

#Generate combined dice roll
def rollTwoDice(dice1, dice2):
  output = random.randint(1,dice1) + random.randint(1,dice2)
  return output

#Print out details
#while True:
print("NAME YOUR CHARACTER")
print("")
char1Name = name()
#Set variables
char1Species = species()
char1Health = rollTwoDice(6,12)/2 + 10
char1Strength = rollTwoDice(6,12)/2 + 12  

time.sleep(0.5)
print("\n"+char1Name, "the", char1Species)
time.sleep(1)
print("Health:", char1Health)
time.sleep(1)
print("Strength:", char1Strength)
time.sleep(1.5)

print("\nWHO ARE THEY FIGHTING?\n")
char2Name = name()
#Set variables
char2Species = species()
char2Health = rollTwoDice(6,12)/2 + 10
char2Strength = rollTwoDice(6,12)/2 + 12  

time.sleep(0.5)
print("\n"+char2Name, "the", char2Species)
time.sleep(1)
print("Health:", char2Health)
time.sleep(1)
print("Strength:", char2Strength)
time.sleep(2)
input("\nPress enter to begin the battle.")
os.system("clear")

print("BATTLE TIME")
print("\nThe battle begins!\n")
time.sleep(1)
os.system("clear")

damage = abs(char1Strength - char2Strength) + 1

for counter in range(1,50):
  char1Dice = random.randint(1,6)
  char2Dice = random.randint(1,6)
  if char1Dice > char2Dice:
    char2Health = max(char2Health - damage, 0.0)
    print(char1Name, "wins round", counter)
    print(char1Name+": "+str(char1Health)+"hp")
    print(char2Name+": "+str(char2Health)+"hp\n")    
  elif char1Dice < char2Dice:
    char1Health = max(char1Health - damage, 0.0)
    print(char2Name, "wins round", counter)
    print(char1Name+": "+str(char1Health)+"hp")
    print(char2Name+": "+str(char2Health)+"hp\n")
  else:
    print( "Round", counter, "is a draw!")
    print(char1Name+": "+str(char1Health)+"hp")
    print(char2Name+": "+str(char2Health)+"hp\n")  
  if char1Health == 0:
    break
    print(char2Name,"wins!")
  if char2Health == 0:
    break
    print(char1Name,"wins!")
  time.sleep(1.5)
  os.system("clear")