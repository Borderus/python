mokeBeast = {}
types = ("Earth", "Fire", "Water", "Air", "Spirit")
typeColours = ("\033[32m", "\033[31m", "\033[34m", "\033[39m", "\033[35m")

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
    
print(typeColours[types.index(mokeBeast["type"])], end='')
print(f"Your beast is called {mokeBeast['name']}.\nIt is {mokeBeast['typeGrammar'].lower()} {mokeBeast['type']} beast with a special move of {mokeBeast['move']}")
print("\033[39m", end='')