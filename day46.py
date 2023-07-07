# Exercise 1
#clue = {}

#def prettyPrint():
#  print()

#  for key, value in clue.items():
#    print(key, end=': ')
#    for subKey, subValue in value.items():
#      print(subKey.title(), subValue.title(), end=" | ")
#    print()

#while True:
#  name = input("Name ")
#  location = input("Location ")
#  weapon = input("Weapon ")

#  clue[name] = {"location": location, "weapon": weapon}

#  prettyPrint()

# Exercise 2

#john = {"daysCompleted": 46, "streak": 22}
#janet = {"daysCompleted": 21, "streak": 21}
#erica = {"daysCompleted": 75, "streak": 6}

#courseProgress = {"John": john, "Janet":janet, "Erica": erica}

#print(courseProgress["Erica"]["daysCompleted"])

#Fix my Code

#john = {"daysCompleted": 46, "streak": 22}
#janet = {"daysCompleted": 21, "streak": 21}
#erica = {"daysCompleted": 75, "streak": 6}

#courseProgress = {"John":john, "Janet":janet, "Erica":erica}

#print(courseProgress["Erica"]["daysCompleted"])
#print(courseProgress["Janet"]["streak"])

#Day 46 Challenge

mokeBeast = {}
mokeDex = {}
types = ("Earth", "Fire", "Water", "Air", "Spirit")
typeColours = ("\033[32m", "\033[31m", "\033[34m", "\033[39m", "\033[35m")

#----------------------BEASTPRINT--------------------------
def beastPrint(mokeBeast):
  print(typeColours[types.index(mokeBeast["type"])], end='')
  print(f"Your beast is called {mokeBeast['name']}.\nIt is {mokeBeast['typeGrammar'].lower()} {mokeBeast['type']} beast with a special move of {mokeBeast['move']}")
  print("\033[39m")

#-----------------------DEXPRINT---------------------------
def dexPrint(mokeDex):
  print()

  for key, value in mokeDex.items():
    print(key, end=': ')
    for subKey, subValue in value.items():
      print(subKey.title(), subValue, end=" | ")
    print()

#-----------------------RUN CODE---------------------------
while True:
  mokeBeast.update({'name':input("What is your MokeBeast's name? ").title()})
  print()

  while True:
    beastType = input("And is your MokeBeast an earth, fire, water, air or spirit type? ").title()
    if beastType in types:
      mokeBeast.update({"type": beastType})
      if beastType == "Earth" or beastType == "Air":
        mokeBeast.update({"typeGrammar": "An"})
      else:
        mokeBeast.update({"typeGrammar": "A"})
      print()
      break
    else:
      print("Type not recognised. Please try again.")

  mokeBeast.update({'move':input("And what is their special move? ").title()})
  print()

  while True:
    hp = int(input("Input your beast's starting HP: "))
    if hp <= 0:
      print("Invalid value - please try again.")
    else:
      mokeBeast.update({"hp": hp})
      print()
      break

  while True:
    mp = int(input("Input your beast's starting MP: "))
    if mp <= 0:
      print("Invalid value - please try again.")
    else:
      mokeBeast.update({"mp": mp})
      print()
      break
  
  beastPrint(mokeBeast)

  loopCheck = input("Again? ")
  if loopCheck.lower().strip()[0] == "n":
    break
  
  mokeDex[mokeBeast["name"]] = mokeBeast
  dexPrint(mokeDex)