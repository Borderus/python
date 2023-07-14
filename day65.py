# Day 65 Challenge

class character:
  def __init__(self, name, health, mana):
    self.name = name
    self.health = health
    self.mana = mana

  def printChar(self):
    print(f"Name: {self.name}")
    print(f"Health: {self.health}")
    print(f"Magic points: {self.mana}")

class player(character):
  def __init__(self, name, health, mana, lives):
    self.name = name
    self.health = health
    self.mana = mana
    self.lives = lives

  def amIAlive(self):
    if self.lives <= 0:
      return False
    else:
      return True

  def print(self):
    self.printChar()
    print(f"Lives: {self.lives}")
    print(f"Alive?: {self.amIAlive()}")

class enemy(character):
  def __init__(self, name, health, mana, type, strength):
    self.name = name
    self.health = health
    self.mana = mana
    self.type = type
    self.strength = strength

  def printEnemy(self):
    self.printChar()
    print(f"Type: {self.type}")
    print(f"Strength: {self.strength}")

class orc(enemy):
  def __init__(self, name, health, mana, strength, speed):
    self.name = name
    self.health = health
    self.mana = mana
    self.type = "Orc"
    self.strength = strength
    self.speed = speed

  def print(self):
    self.printEnemy()
    print(f"Speed: {self.speed}")

class vampire(enemy):
  def __init__(self, name, health, mana, strength, dayNightInd):
    self.name = name
    self.health = health
    self.mana = mana
    self.type = "Vampire"
    self.strength = strength
    self.dayNightInd = dayNightInd

  def print(self):
    self.printEnemy()
    print(f"Day/Night?: {self.dayNightInd}")

# Instantiation

dave = player("Ted", 100, 50, 3)
boris = vampire("Boris", 45, 70, 3, "Night")
rishi = vampire("Rishi", 70, 10, 75, "Day")
bill = orc("Bill", 60, 5, 75, 90)
ted = orc("Ted", 75, 40, 80, 45)
station = orc("Station", 35, 40, 49, 50)

dave.print()
print()
boris.print()
print()
rishi.print()
print()
bill.print()
print()
ted.print()
print()
station.print()