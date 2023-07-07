#Baby Animals
#Initialise
import os, time, random

deck = {}
deck["Baby Panda"] = {"Card": "Baby Panda", "Mommy's Tummy": 5, "Birthweight": 1, "Independence": 8, "Mischief": 5, "Cuteness": 5}
deck["Baby Duck"] = {"Card": "Baby Duck","Mommy's Tummy": 1, "Birthweight": 0.5, "Independence": 7, "Mischief": 5, "Cuteness": 5}
deck["Baby Gorilla"] = {"Card": "Baby Gorilla","Mommy's Tummy": 9, "Birthweight": 4, "Independence": 3, "Mischief": 29, "Cuteness": 3}

deckList = []

print("Baby Animals Top Trumps!")
print()
print("Pick your card:")
for key, value in deck.items():
  deckList.append(key)
  print("    "+str(deckList.index(key))+": "+key)

print()
cardchoice = int(input("> "))
playerCard = deck[deckList[cardchoice]]
opponentCard = deck[deckList[(cardchoice+random.randint(1, len(deck)-1))%len(deck)]]

os.system("clear")

print("Pick your attribute:")
for key in playerCard.keys():
  if key != "Card":
    print("- "+key)
print()
attribute = input("> ")

os.system("clear")

print("\n")
time.sleep(0.5)
print(f"{playerCard['Card']}: {attribute} stat of {playerCard[attribute]}")
time.sleep(0.7)
print()
print(f"{opponentCard['Card']}: {attribute} stat of {opponentCard[attribute]}")
time.sleep(0.7)

print("\n")
if playerCard[attribute] > opponentCard[attribute]:
  print(f"{playerCard['Card']} wins!")
elif playerCard[attribute] < opponentCard[attribute]:
  print(f"{opponentCard['Card']} wins!")
else:
  print("It's a draw!")
