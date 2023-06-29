#Exercise 1
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}
#Method to get keys
#for i in myDictionary.keys():
#  print(i)
#Method to get values
#for i in myDictionary.values():
#  print(i)
#Method to get key-value pairs
#for name, value in myDictionary.items():
#  print(f"{name}:{value}")

#for name, value in myDictionary.items():
#  print(f"{name}:{value}")

#  if (name == "strength") and (value >= 100):
#    print()
#    print("Whoa, SO STRONG!")
#    print()

myDictionary = {"name" : "David the Mildly Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

#for name, value in myDictionary.items():
#  print(f"{name}:{value}")

#  if (name == "strength"):
#    if value > 100:
#      print("Whoa, SO STRONG!")
#    else:
#      print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")

#Day 41 Challenge

websiteRating = {}

websiteRating.update({"name": input("Input the website name\n")})
print()
websiteRating.update({"url": input("Input the URL\n")})
print()
websiteRating.update({"description": input("Input a star rating out of 5\n")})

print()
for key, value in websiteRating.items():
  print(f"{key}: {value}")