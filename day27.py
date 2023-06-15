#Day 27 Challenge

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

#Set variables
species = species()
health = rollTwoDice(6,12)/2 + 10
strength = rollTwoDice(6,12)/2 + 12

#Print out details
while True:
  print("Character builder ")
  print("")
  charName = name()
  os.system("clear")

  time.sleep(0.5)
  print(charName, "the", species)
  time.sleep(1)
  print("Health:", health)
  time.sleep(1)
  print("Strength:", strength)
  time.sleep(1.5)
  print("")
  print("May your name go down in legend...")
  time.sleep(1)
  print("")
  restart = input("Generate a new character? ")
  if restart.lower() == "no":
    break
  os.system("clear")